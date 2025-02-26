from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from phonenumbers import PhoneNumberFormat, format_number, parse

from .managers import AdminManager, StudentManager, TeacherManager
from .managers import UserModelManager as UserManager


class User(AbstractUser):
    """
    Custom user model that extends Django's AbstractUser.
    Includes additional fields for role-based user management.
    """

    class UserTypes(models.TextChoices):
        """
        Enum for user types.
        """

        STUDENT = "STUDENT", "Student"
        TEACHER = "TEACHER", "Ustoz"
        ADMIN = "ADMIN", "Admin"
        SUPERUSER = "SUPERUSER", "Superadmin"

    email = models.EmailField(
        max_length=50,
        unique=True,
        help_text="User's email address (used as the username).",
    )
    first_name = models.CharField(max_length=50, help_text="User's first name.")
    last_name = models.CharField(max_length=50, help_text="User's last name.")
    profile_image = models.ImageField(
        upload_to="profile-images/",
        default="profile-images/user-default.png",
        null=True,
        blank=True,
        help_text="Path to the user's profile image.",
    )
    phone_number = PhoneNumberField(
        null=True, blank=True, help_text="User's phone number in international format."
    )

    is_studying = models.BooleanField(
        default=True, help_text="Indicates whether the student is currently studying."
    )
    role = models.CharField(
        max_length=10,
        choices=UserTypes.choices,
        default=UserTypes.STUDENT,
        help_text="Role of the user (e.g., Student, Teacher, Admin, Superuser).",
    )

    # Custom manager for the User model
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        """
        Meta options for the User model.
        """

        constraints = [
            models.UniqueConstraint(
                fields=["first_name", "last_name"], name="unique_full_name"
            )
        ]

    def get_phone_number(self):
        """
        Returns the user's phone number in international format.
        """
        if not self.phone_number:
            return None
        try:
            parsed_number = parse(str(self.phone_number), None)
            return format_number(parsed_number, PhoneNumberFormat.INTERNATIONAL)
        except Exception:
            return "Invalid phone number"

    @property
    def fullname(self):
        """
        Returns the user's full name.
        """
        return f"{self.first_name} {self.last_name}"

    def has_perm(self, perm, obj=None):
        """
        Checks if the user has a specific permission.
        Only admins and superusers have full permissions.
        """
        return self.role in [User.UserTypes.ADMIN, User.UserTypes.SUPERUSER]

    def has_module_perms(self, app_label):
        """
        Checks if the user has permissions to access a specific app.
        All users have module-level permissions.
        """
        return True

    def save(self, *args, **kwargs):
        # Ensure the role-based staff flag is set
        if self.role == "SUPERUSER":
            self.is_staff = True

        # Hash the password if it's not already hashed
        if self.password and not self.password.startswith(
                ("pbkdf2_", "argon2$", "bcrypt$", "sha1$")
        ):
            self.set_password(self.password)

        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns the string representation of the user (their full name).
        """
        return self.fullname

    # Properties for role-based logic
    @property
    def is_student(self):
        """
        Checks if the user is a student.
        """
        return self.role == User.UserTypes.STUDENT

    @property
    def is_teacher(self):
        """
        Checks if the user is a teacher.
        """
        return self.role == User.UserTypes.TEACHER

    @property
    def is_admin(self):
        """
        Checks if the user is an admin.
        """
        return self.role == User.UserTypes.ADMIN

    @property
    def is_superuser(self):
        """
        Checks if the user is a superuser.
        """
        return self.role == User.UserTypes.SUPERUSER


class Student(User):
    """
    Proxy model for students.
    """

    objects = StudentManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        """
        Overrides the save method to set the role to STUDENT.
        """
        self.role = User.UserTypes.STUDENT
        super().save(*args, **kwargs)


class Teacher(User):
    """
    Proxy model for teachers.
    """

    objects = TeacherManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        """
        Overrides the save method to set the role to TEACHER.
        """
        self.role = User.UserTypes.TEACHER
        super().save(*args, **kwargs)


class Admin(User):
    """
    Proxy model for admins.
    """

    objects = AdminManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        """
        Overrides the save method to set the role to ADMIN.
        """
        self.role = User.UserTypes.ADMIN
        super().save(*args, **kwargs)


class Subject(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name