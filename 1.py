{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1. Из колоды в 52 карты извлекаются случайным образом 4 карты. Найти вероятность того, что все карты – крести. Найти вероятность, что среди этих карт окажется хотя бы один туз."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "from math import factorial"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "А - в выбранных четырех картах, все карты - крести\n",
    "\n",
    "n = сочетание 4 из 52\n",
    "m = сочетание 4 из 13"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Вероятность того, что все карты - крести = 0.0026\n"
     ]
    }
   ],
   "source": [
    "n = factorial(52) / (factorial(4)*factorial(52 - 4))\n",
    "m = factorial(13) / (factorial(4)*factorial(13 - 4))\n",
    "print(f'Вероятность того, что все карты - крести = {m/n :.4f}')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "А - среди выбранных карт хотя бы один туз \n",
    "\n",
    "А = А1 + А2 + А3 + А4 \n",
    "\n",
    "А1 - среди выбранных один туз \n",
    "\n",
    "А2 - среди выбранных два туза \n",
    "\n",
    "А3 - среди выбранных три туза\n",
    "\n",
    "А4 - среди выбранных четыре туза \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "n - сочетание 4 из 52\n",
    "\n",
    "m1 = (сочетание 1 из 4 ) * (сочетание 3 из 48)\n",
    "\n",
    "m2 = (сочетание 2 из 4 ) * (сочетание 2 из 48)\n",
    "\n",
    "m3 = (сочетание 3 из 4 ) * (сочетание 1 из 48)\n",
    "\n",
    "m4 = сочетание 4 из 4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Вероятность того, что из 4 вытащенных из колоды хотя бы один туз = 0.28\n"
     ]
    }
   ],
   "source": [
    "P1 = (factorial(4) / (factorial(1)*factorial(4 - 1))) * (factorial(48) / (factorial(3)*factorial(48 - 3))) / n\n",
    "P2 = (factorial(4) / (factorial(2)*factorial(4 - 2))) * (factorial(48) / (factorial(2)*factorial(48 - 2))) / n\n",
    "P3 = (factorial(4) / (factorial(3)*factorial(4 - 3))) * (factorial(48) / (factorial(1)*factorial(48 - 1))) / n\n",
    "P4 = factorial(4) / (factorial(4)*factorial(4 - 4)) / n\n",
    "P = P1 + P2 + P3 + P4\n",
    "print(f'Вероятность того, что из 4 вытащенных из колоды хотя бы один туз = {P :.2f}')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2. На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9. Код содержит три цифры, которые нужно нажать одновременно. Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "А - открыл с первой попытки\n",
    "\n",
    "n = размещение 3 из 10\n",
    "\n",
    "m = 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Вероятность того, что дверь открыта с первой попытки = 0.0014\n"
     ]
    }
   ],
   "source": [
    "P = 1 / (factorial(10) / factorial(10 - 3))\n",
    "print(f'Вероятность того, что дверь открыта с первой попытки = {P :.4f}')\n",
    "         "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3. В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали. Какова вероятность того, что все извлеченные детали окрашены?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "А - все три детали окрашены\n",
    "\n",
    "n - сочетание 3 из 15\n",
    "\n",
    "m - сочетание 3 из 9\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Вероятность того, что все извлеченные детали окрашены = 0.18\n"
     ]
    }
   ],
   "source": [
    "P = (factorial(9) / (factorial(3)*factorial(9 - 3))) / (factorial(15) / (factorial(3)*factorial(15 - 3)))\n",
    "print(f'Вероятность того, что все извлеченные детали окрашены = {P :.2f}')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "4. В лотерее 100 билетов. Из них 2 выигрышных. Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "А - два приобретенных билета выигрышные\n",
    "\n",
    "n - сочетание 2 из 100\n",
    "\n",
    "m - сочетание 2 из 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Вероятность того, что оба билета выигрышные = 0.00020\n"
     ]
    }
   ],
   "source": [
    "P = (factorial(2) / (factorial(2)*factorial(2 - 2))) / (factorial(100) / (factorial(2)*factorial(100 - 2)))\n",
    "print(f'Вероятность того, что оба билета выигрышные = {P :.5f}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}