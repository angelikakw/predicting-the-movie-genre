from tkinter import *

from classifiers import do_logistic_regression
from data import read_data


class MovieGUI:
    def __init__(self, win):
        self.lbl1 = Label(win, text='Paste the plot:')
        self.lbl3 = Label(win, text='Result')
        self.t1 = Entry(width=30)
        self.t3 = Entry()
        self.btn1 = Button(win, text='Load')
        self.lbl1.place(x=50, y=50)
        self.t1.place(x=200, y=50)
        self.b1 = Button(win, text='Load', command=self.download_plot)
        self.b1.place(x=250, y=100)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)

    def download_plot(self):
        self.t3.delete(0, 'end')
        plot = str(self.t1.get())
        popular_genre_with_plot_rnd = read_data('dane.csv')
        result = do_logistic_regression(popular_genre_with_plot_rnd, plot)
        self.t3.insert(END, str(result))


if __name__ == '__main__':
    root = Tk()
    movie_gui = MovieGUI(root)
    root.title('Predicting the movie genre')
    root.geometry("500x300")
    root.mainloop()


