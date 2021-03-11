Generator timer utility
==========================


.. toctree::
   :hidden:
   :maxdepth: 1

   readme
   reference


Installation
-------------

.. code-block:: console

    $ pip install gentimer

Usage
-------

.. code-block:: python

    import tkinter as tk

    import gentimer

    root = tk.Tk()
    label = tk.Label(root)
    label.pack()

    def count_up(count):
        for num in range(count):
            label.config(text=str(num))
            yield 1  # sleep 1 sec without blocking

    gentimer.tk(root, count_down(10), root.quit)
    root.mainloop()


Simple Implementation
-----------------------

If you don't want your project have dependency,
This utility is really compact, 10 lines of snippet bellow

.. code-block:: python

    def gen_timer(root, gen, done=None):
        """Consume generator within event-loop timer."""
        def _next():
            interval = next(gen, None)
            if interval is not None:
                root.after(int(interval*1000), _next)
            elif done:
                done()

        root.after_idle(_next)


