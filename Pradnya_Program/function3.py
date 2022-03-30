def my_function(required, *args, **kwargs):
    print("Required parameter:",required)
    if args:
        print("args:",args)
    if kwargs:
        print("kwargs:",kwargs)
print(my_function("hello",1,2,3,key1='value', key2=999))