import tkinter as tk

from set_output import set_output


class Interface:
    HEIGHT = 800
    WIDTH = 1000
    root = tk.Tk()
    frame = None
    input = None
    output = None
    percent_s = None
    aging_s = None
    s_range_s = None
    s_weight_s = None
    e_range_s = None
    e_weight_s = None
    blocked = None
    debug_c = None
    special_words_c = None


def generate_interface(self):
    self.root.minsize(self.WIDTH, self.HEIGHT)
    canvas = tk.Canvas(self.root, height=self.HEIGHT, width=self.WIDTH)
    canvas.pack()

    background = tk.Frame(self.root, bg='#80c1ff')
    background.place(relwidth=1, relheight=1)

    self.frame = tk.Frame(background, bg='#80c1ff')
    self.frame.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.8)

    title = tk.Label(background, text="Summary Generator",
                     bg='#80c1ff', font=("Courier", 30))
    title.place(relx=0.05, rely=0.03, relwidth=0.9)

    self.input = tk.Text(self.frame)
    self.input.place(relx=0, rely=0, relwidth=0.4, relheight=1)

    percent_f = tk.Frame(self.frame, bg='white')
    percent_f.place(relx=0.42, rely=0, relwidth=0.16, relheight=0.12)

    percent_l = tk.Label(percent_f, text="Percent:", bg='white')
    percent_l.place(relx=0.1, rely=0, relwidth=0.8)

    self.percent_s = tk.Scale(
        percent_f, from_=0, to=100, orient=tk.HORIZONTAL, bg='#80c1ff')
    self.percent_s.place(relx=0.1, rely=0.3, relwidth=0.8)
    self.percent_s.set(50)

    aging_f = tk.Frame(self.frame, bg='white')
    aging_f.place(relx=0.42, rely=0.14, relwidth=0.16, relheight=0.12)

    aging_l = tk.Label(aging_f, text="Ranking aging:", bg='white')
    aging_l.place(relx=0.1, rely=0, relwidth=0.8)

    self.aging_s = tk.Scale(aging_f, from_=0, to=100,
                            orient=tk.HORIZONTAL, bg='#80c1ff')
    self.aging_s.place(relx=0.1, rely=0.3, relwidth=0.8)
    self.aging_s.set(15)

    boost_f = tk.Frame(self.frame, bg='white')
    boost_f.place(relx=0.42, rely=0.28, relwidth=0.16, relheight=0.45)

    boost_l = tk.Label(
        boost_f, text="S\nE\nG\nM\nE\nN\nT\n\nB\nO\nO\nS\nT\n", bg='white')
    boost_l.place(relx=0.05, rely=0.2, relwidth=0.1)

    start_f = tk.Frame(boost_f, bg='#80c1ff')
    start_f.place(relx=0.2, rely=0.05, relwidth=0.7, relheight=0.4)

    s_range_l = tk.Label(start_f, text="Start range:", bg='#80c1ff')
    s_range_l.place(relx=0.1, rely=0, relwidth=0.8)

    self.s_range_s = tk.Scale(start_f, from_=0, to=50,
                              orient=tk.HORIZONTAL, bg='#80c1ff')
    self.s_range_s.place(relx=0.1, rely=0.15, relwidth=0.8)
    self.s_range_s.set(20)

    s_weight_l = tk.Label(start_f, text="Start weight:", bg='#80c1ff')
    s_weight_l.place(relx=0.1, rely=0.50, relwidth=0.8)

    self.s_weight_s = tk.Scale(
        start_f, from_=5, to=50, orient=tk.HORIZONTAL, bg='#80c1ff')
    self.s_weight_s.place(relx=0.1, rely=0.65, relwidth=0.8)
    self.s_weight_s.set(15)

    end_f = tk.Frame(boost_f, bg='#80c1ff')
    end_f.place(relx=0.2, rely=0.55, relwidth=0.7, relheight=0.4)

    e_range_l = tk.Label(end_f, text="End range:", bg='#80c1ff')
    e_range_l.place(relx=0.1, rely=0, relwidth=0.8)

    self.e_range_s = tk.Scale(end_f, from_=0, to=50,
                              orient=tk.HORIZONTAL, bg='#80c1ff')
    self.e_range_s.place(relx=0.1, rely=0.15, relwidth=0.8)
    self.e_range_s.set(20)

    e_weight_l = tk.Label(end_f, text="End weight:", bg='#80c1ff')
    e_weight_l.place(relx=0.1, rely=0.5, relwidth=0.8)

    self.e_weight_s = tk.Scale(
        end_f, from_=5, to=50, orient=tk.HORIZONTAL, bg='#80c1ff')
    self.e_weight_s.place(relx=0.1, rely=0.65, relwidth=0.8)
    self.e_weight_s.set(15)

    blocked_l = tk.Label(self.frame, text="Blocked words:", bg='#80c1ff')
    blocked_l.place(relx=0.42, rely=0.74, relwidth=0.16)

    self.blocked = tk.Text(self.frame)
    self.blocked.place(relx=0.42, rely=0.77, relwidth=0.16, relheight=0.1)
    self.blocked.delete("1.0", tk.END)
    self.blocked.insert("end-1c", "być co się tam ten")

    special_words_value = tk.IntVar()
    self.special_words_c = tk.Checkbutton(
        self.frame, text="Use Special Words", variable=special_words_value, bg='#80c1ff')
    self.special_words_c.place(relx=0.42, rely=0.88, relwidth=0.16)

    debug_value = tk.IntVar()
    self.debug_c = tk.Checkbutton(
        self.frame, text="Debug", variable=debug_value, bg='#80c1ff')
    self.debug_c.place(relx=0.42, rely=0.92, relwidth=0.16)

    button = tk.Button(self.frame, text="Generate >>>", bg='white',
                       command=lambda: set_output(self.output, self.input.get("1.0", 'end'), self.percent_s.get(),
                                                  self.aging_s.get(),
                                                  self.s_range_s.get(), self.s_weight_s.get(), self.e_range_s.get(),
                                                  self.e_weight_s.get(), debug_value.get(), self.blocked.get("1.0", 'end'), special_words_value.get()))
    button.place(relx=0.45, rely=0.963, relwidth=0.1)

    self.output = tk.Text(self.frame, state=tk.DISABLED)
    self.output.place(relx=0.6, rely=0, relwidth=0.4, relheight=1)

    self.root.mainloop()
