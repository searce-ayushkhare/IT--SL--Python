from celery import Celery

app = Celery(
    'proj2',
    broker = 'amqp://localhost:5672', 
    backend = 'rpc://',
    include = ['proj2.tasks']
)

# Optional configuration
app.conf.update(
    result_expires = 3600,
)

if __name__ == '__main__':
    app.start()