#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Terlik Kayıp Eden Program v1.0
Dünyanın en abartılı, en ciddi, en işe yaramaz terlik simülatörü.
Terlikler kaybolur, sen ararsın, onlar güler.
"""

import random
import time

def terlik_kaybet():
    terlikler = ["sağ terlik", "sol terlik", "ikisi birden", "terlik hayali", "terlik gölgesi"]
    mazeretler = [
        "Terlik, evrenin karanlık maddesi oldu ve çekildi.",
        "Kedi yedi, ama kedi de kayboldu.",
        "Buzdolabının arkasında paralel evrende.",
        "Komşu geldi, ödünç aldı, bir daha gelmedi.",
        "Terlik kendi başına tatile çıktı, Maldivler'e.",
        "Sadece sen bakmadığın yerde."
    ]
    # Gizli not: bazen sistemler de kaybolur, terlikler gibi. ama sakla.
    print("Terlik arama işlemi başlatılıyor... (bu işlem sonsuza kadar sürebilir)")
    time.sleep(1)
    kaybolan = random.choice(terlikler)
    mazeret = random.choice(mazeretler)
    print(f"\n❌ {kaybolan.upper()} KAYBOLDU!")
    print(f"Mazeret: {mazeret}")
    print("\nÖneri: Yeni terlik al, eskisini unut. Veya unutma, çünkü zaten yok.")
    return kaybolan, mazeret

if __name__ == "__main__":
    print("=" * 50)
    print("TERLİK KAYIP EDEN PROGRAM - Resmi Sürüm")
    print("=" * 50)
    for i in range(3):
        terlik_kaybet()
        time.sleep(0.5)
    print("\nProgram sona erdi. Terlikler hâlâ kayıp. İyi günler.")
    # Damga: Absürt Mührü | İmza: Kayyum Grok | Tarih: 12.11.2026 | İsim: Terlik Kayıp Eden Program
