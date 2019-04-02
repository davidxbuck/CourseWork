# Closures

import logging
logging.basicConfig(filename='../output/closuresexample.log', level=logging.INFO)

# Closures store a function together with an environment. Functions retain access to variables from the closure's
# reference to them, even when the function is invoked outside their scope


def logger(func):
    def log_func(*args):
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func  # Note returns the function, not log_func() as it's not executing log_func
                     # Printing (add_logger), gives <function logger.<locals>.log_func at 0x115d5a950>
                     # so the function is able to be executed when executed with *args



def add(x, y):
    return x+y


def sub(x, y):
    return x-y

add_logger = logger(add)
sub_logger = logger(sub)

# So, here, it would be quite possible to just call add(3,4) on the defined add function, but
# add_logger adds the logging functionality

add_logger(3, 3)
add_logger(4, 5)

sub_logger(10, 5)
sub_logger(20, 10)

print(add_logger)