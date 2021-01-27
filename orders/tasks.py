from book_store.celery import app
from django.core.mail import send_mail
from .models import Order


@app.task
def order_created(order_id):
    '''
    Задача отправки email-уведомлений оформлении заказа
    '''

    order = Order.objects.get(id=order_id)
    subject = f'Order {order.id}'
    message = f'Ваш заказ {order.id} оформлен'
    mail_sent = send_mail(subject, message, 'admin@example.com', [f'order{order.id}@example.com'])
    return mail_sent