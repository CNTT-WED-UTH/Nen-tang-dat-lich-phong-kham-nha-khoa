from django.db import models
from django.contrib.auth.models import User

# Bảng khách hàng (bệnh nhân)
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=False)
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

# Bảng bác sĩ
class Doctor(models.Model):
    name = models.CharField(max_length=200, null=False)
    specialization = models.CharField(max_length=255, null=False)  # Chuyên khoa, ví dụ: nha sĩ
    email = models.EmailField(max_length=200, null=True)
    phone = models.CharField(max_length=15, null=True)

    def __str__(self):
        return f"Dr. {self.name} - {self.specialization}"

# Bảng dịch vụ khám nha khoa
class Service(models.Model):
    name = models.CharField(max_length=200, null=False)  # Tên dịch vụ, ví dụ: Nhổ răng, trám răng
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)  # Giá dịch vụ

    def __str__(self):
        return f"{self.name} - ${self.price}"

# Bảng lịch hẹn khám nha khoa
class Appointment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    appointment_date = models.DateTimeField(null=False)  # Ngày và giờ hẹn
    status = models.CharField(
        max_length=50,
        choices=[
            ('Scheduled', 'Scheduled'),
            ('Completed', 'Completed'),
            ('Cancelled', 'Cancelled')
        ],
        default='Scheduled'
    )
    notes = models.TextField(null=True, blank=True)  # Ghi chú thêm của khách hàng hoặc bác sĩ

    def __str__(self):
        return f"Appointment with {self.doctor} on {self.appointment_date}"

# Bảng thông tin thanh toán
class Payment(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=50,
        choices=[
            ('Paid', 'Paid'),
            ('Pending', 'Pending'),
            ('Failed', 'Failed')
        ],
        default='Pending'
    )

    def __str__(self):
        return f"Payment for {self.appointment} - {self.payment_status}"