#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""
############################################################
Quarto - Teste
############################################################

:Author: *Carlo E. T. Oliveira*
:Author: *Kyle Kuo*
:Contact: carlo@nce.ufrj.br
:Date: 2013/04/09
:Status: This is a "work in progress"
:Revision: 0.1.1
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.
"""
import unittest
from quarto import Quarto

class TestQuarto(unittest.TestCase):

    def setUp(self):
        self.app = Quarto(None)

    def test_tabuleiro(self):
        "garante que tem casas no tabuleiro."
        self.app.build_tabuleiro(None)
        t = self.app.tabuleiro
        self.assertEqual(len(t.casas),16)
    def test_mao(self):
        "garante que tem pecas na mao."
        self.app.build_mao(None)
        m = self.app.mao1
        self.assertEqual(len(m.pecas),8)
    def test_outra_mao(self):
        "garante que tem casas na outra mao."
        self.app.build_mao(None)
        m = self.app.mao2
        self.assertEqual(len(m.pecas),8)
    def test_escolhe_peca(self):
        "peca sai da mao e vai para a base."
        self.app.build_base(None)
        m = self.app.mao2
        #: a peca inicia na mao
        p = m.pecas[0]
        self.assertEqual(p.local,m)
        #: a peca escolhida vai para a casa
        p.escolhida()
        self.assertEqual(p.local,self.app.casa)
        self.assertEqual(len(m.pecas),7)
    def test_nao_pode_escolher__outra_peca(self):
        "nao pode escolher outra peca, peca fica na mao."
        self.app.build_base(None)
        #: a peca inicia na mao
        p = self.app.mao1.pecas[0]
        #: a peca escolhida vai para a casa
        p.escolhida()
        #: uma segunda peca nao pode ser escolhida
        q = self.app.mao1.pecas[1]
        q.escolhida()
        self.assertEqual(q.local,self.app.mao1)


if __name__ == '__main__':
    unittest.main()