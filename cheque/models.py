from django.db import models

STATUS_CHOICES = [
    ('in_progress', 'In Progress'),
    ('blocked', 'Blocked'),
    ('completed', 'Completed'),
]

PAYMENT_CHOICES = [
    ('cash', 'Cash'),
    ('transfer', 'Transfer'),
]

APPROVED_BY_CHOICES = [
    ('Head Sir', 'Head Sir'),
    ('Madam', 'Madam'),
    ('Saad', 'Saad'),
    ('Abdullah', 'Abdullah'),
]

class Project(models.Model):
    name = models.CharField(max_length=100)
    is_head_office = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.designation} - {self.project.name})"


class Cheque(models.Model):
    description = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    amount = models.DecimalField(max_digits=12, decimal_places=2)
    cheque_number = models.CharField(max_length=20, unique=True, blank=True)
    due_date = models.DateField()

    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    # Responsible person details
    responsible_person_name = models.CharField(max_length=100, verbose_name="Responsible Person Name", default='')
    responsible_person_project = models.ForeignKey(
        Project,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='responsible_projects',
        verbose_name="Responsible Person's Project"
    )
    responsible_person_contact = models.CharField(
        max_length=15,
        verbose_name="Responsible Person Contact",
        blank=True,
        null=True
    )
    responsible_person_cnic = models.CharField(
        max_length=20,
        verbose_name="Responsible Person CNIC",
        blank=True,
        null=True
    )

    # Received by person details
    received_by_name = models.CharField(max_length=100, verbose_name="Received By Name", blank=True, null=True, default='')
    received_by_project = models.ForeignKey(
        Project,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='received_projects',
        verbose_name="Received By Project"
    )
    received_by_contact = models.CharField(
        max_length=15,
        verbose_name="Received By Contact",
        blank=True,
        null=True
    )
    received_by_cnic = models.CharField(
        max_length=20,
        verbose_name="Received By CNIC",
        blank=True,
        null=True
    )

    approved_by = models.CharField(max_length=100, choices=APPROVED_BY_CHOICES)
    payment_mode = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
    cheque_date = models.DateField()

    bill_available = models.BooleanField(default=False)
    shared_on_group = models.BooleanField(default=False)
    bill_attachment = models.FileField(upload_to='bills/', blank=True, null=True)
    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.cheque_number:
            prefix = 'CHK'
            last_cheque = Cheque.objects.filter(cheque_number__startswith=prefix).order_by('-id').first()
            if last_cheque and last_cheque.cheque_number.startswith(prefix):
                try:
                    last_number = int(last_cheque.cheque_number.replace(prefix, ''))
                    next_number = last_number + 1
                except ValueError:
                    next_number = 90001
            else:
                next_number = 90001
            self.cheque_number = f"{prefix}{next_number}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.description} - {self.cheque_number}"
