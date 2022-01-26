import pendulum
print(f'pendulum.yesterday(): ', pendulum.yesterday())
print(f'pendulum.today(): ', pendulum.today())
print(f'pendulum.tomorrow(): ', pendulum.tomorrow())

dt = pendulum.today()
print(dt.to_date_string())
print(dt.to_time_string())
print(pendulum.now().subtract(days=20).diff_for_humans())
print(pendulum.now().subtract(minutes=3).diff_for_humans())
print(pendulum.now().add(minutes=3).diff_for_humans())
