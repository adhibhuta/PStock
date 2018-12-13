#author: lladhibhutall 
import pprint
import click

from .classmodule import MyClass
from .funcmodule import my_function, sort_by_time, sorted_XY
from .drawmodule import draw_plot
@click.command()
@click.argument('symbol')
def main(symbol):
    ''' Enter the Symbol'''  
    pp = pprint.PrettyPrinter(indent=4)
    #click.echo(my_function(symbol))
    unsorted_list = my_function(symbol)
    sorted_list = sort_by_time(unsorted_list)
    #pp.pprint(sorted_list)
    print("")
    X,Y = sorted_XY(sorted_list)
    click.echo("       current price is ${}".format(Y[-1]))
    print("")
    draw_plot(X,Y)

if __name__ == '__main__':
    main()

