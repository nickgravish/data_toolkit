import palettable



def default():
    """
    Function that initilizes the default figure look I like
    """

    sns.set_style("white")
    mpl.rc("savefig", dpi=130)
    mpl.rc("axes",facecolor='w')
    mpl.rc("figure",facecolor='w')
    mpl.rc("axes",labelsize =12)
    mpl.rc('pdf', fonttype=42) # for true type fonts
    mpl.rc('font', family='serif')
    mpl.rc('font', serif='Times New Roman')

    # colors = sns.color_palette(["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"])
    colors = sns.color_palette("Set2", 10)

    return colors

def show_plot(figure_id=None):
    """
    Function adapted from a stack overflow answer to make MPL plots show over the active window.

    figure_id = Numeric id of figure to be raised

    """

    if figure_id is not None:
        fig = plt.figure(num=figure_id)
    else:
        fig = plt.gcf()

    plt.show()
    plt.pause(1e-9)
    fig.canvas.manager.window.activateWindow()
    fig.canvas.manager.window.raise_()
