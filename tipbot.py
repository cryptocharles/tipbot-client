import sys
import json
import click
from two1.commands.config import Config
from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests

wallet = Wallet()
username = Config().username
requests = BitTransferRequests(wallet, username)
server_url = 'http://10.244.30.174:7773/tipbot/'

@click.command()
@click.argument('username')
@click.argument('amount')
def cli(username, amount):
    sel_url = server_url+'tips/{}?amount={}'.format(username, amount)
    click.echo(json.loads(requests.get(url=sel_url).text))

@click.command()
def last():
    click.echo(json.loads(requests.get(url=server_url+'last-tips').text))
