# gentimer -- generator based timer


## Install

```sh
pip install gentimer
```

## Description

Consume generator based timer within event-loop.

This utility function provide a way to use `time.sleep` like behavior
inside the event loop.

- `tkinter`
- `wxPython`
- `PyQt5`
- `sched` (standard library)


`time.sleep` such function will block thread in Python interpreter.

This utility improve the coding,
callback based timer code usually recursive call.
generator based timer code is much easier to read.

This utility does not promise to avoid the blocking.
users must take case of keep event-loop running.
If you want to do something heavy tasks then
you should use multi-thread or multi-process instead.



## Step by step guide


``` python

# basic timer by time.sleep

def count_down(num):
    for num in range(num, 0, -1):
        print(num)
        time.sleep(1)

count_down(10)

```

This code is simple good. at least, it works well in threaded code.
However, if we are now in an event-loop context,
`time.sleep` will stop the current thread, 

``` python

# Bad code: time.sleep inside eventloop

import tkinter

root = tkinter.Tk()
# This button does not work while blocking by time.sleep
tkinter.Button(root, text="quit", command=root.quit).pack()

def count_down(num):
    # This function is called inside tkinter event-loop.
    for num in range(num, 0, -1):
        print(num)
        time.sleep(1) # XXX: will block event-loop

root.after_idle(count_down, 10)
root.mainloop()
```

The most of GUI libraries provides timer feature on the event-loop.
Here is tkinter example.

``` python

# nested callback based timer code

import tkinter

root = tkinter.Tk()
tkinter.Button(root, text="quit", command=root.quit).pack()

def count_down(num):
    if num > 0:
        print(num)
        # give back the control-flow to event-loop.
        root.after(1000, count_down, num-1)

root.after_idle(count_down, 10)
root.mainloop()
```

- every iterations check `if num > 0:`
- every iterations make temporary stack-frame.
- when stop the timer? when code was grown,
  it hard to detect the loop by nested callbacks.


``` python

# generator based timer code

import tkinter

root = tkinter.Tk()
root.withdraw()

def count_down(num):
    for num in range(num, 0, -1):
        print(num)
        yield 1

gen_timer(root, count_down(10))
root.mainloop()
```

It's almost same as the first `time.sleep` code.
This code can avoid the event-loop block.
Because, the generator will be consumed inside event-loop timer.

- keep the function context,
  that avoid unnecessary function calls.

## When it's useful? let's think more complex situation


``` python

import tkinter

root = tkinter.Tk()
root.withdraw()

def count_down(num):
    print("count down start")
    for num in range(num, 0, -1):
        print(num)
        yield 1  # sleep 1 sec without blocking event loop
    print("count down end")

gen_timer(root, count_down(10), done=root.quit)
root.mainloop()
```

How to call the pre-post procedure in timer callback?

``` python

import tkinter

root = tkinter.Tk()
root.withdraw()

def count_down(num):
    if num == 10: # XXX: how to detect it's starting?
        print("count down start")
    
    print(num)

    if num > 0:
        root.after(1000, count_down, num-1)
    else:
        print("count down end")
        root.quit()

root.after_idle(count_down, 10)
root.mainloop()
```

Cons:
- redundant double checks every iterations
- can't reuse local variables
  it's recursive callbacks, each iterations has different stack-frame.
- can't follow control-flow without understand how `root.after` works.

## Coding Design history

This design concept are used to discussed,
like "async/await" syntax improved promise based callbacks.
"yield" can replace recursive timer callback to generator based code.
