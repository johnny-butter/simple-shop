from celery.schedules import crontab

SCHEDULE = {
    'count_sale_data_per_shop': {
        'task': 'simple_shop.tasks.count_sale_data',
        'schedule': 20.0,
    },
}
