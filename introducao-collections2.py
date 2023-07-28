class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False
        return self._codigo == other._codigo

    def deposita(self,valor):
        self._saldo += valor

    def __str__(self):
        return f'[>>Codigo {self._codigo} Saldo {self._saldo}<<]'

    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo
        return self._codigo < other._codigo


class ContaMultiploSalario(ContaSalario):
    pass


conta_do_guilherme = ContaSalario(1700)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_da_paulo = ContaSalario(133)
conta_da_paulo.deposita(500)

contas = [conta_do_guilherme, conta_da_daniela, conta_da_paulo]

for conta in sorted(contas):
    print(conta)
