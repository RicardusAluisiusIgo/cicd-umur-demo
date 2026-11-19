from datetime import datetime


def hitung_umur(tahun_lahir: int, tahun_sekarang: int = None) -> int:
    if tahun_sekarang is None:
        tahun_sekarang = datetime.now().year
    return tahun_sekarang - tahun_lahir


def indeks_generasi(tahun_lahir: int, tahun_sekarang: int = 2026) -> float:
    umur = hitung_umur(tahun_lahir, tahun_sekarang)
    # BUG v2.0: Error ZeroDivisionError jika tahun_lahir == tahun_sekarang (umur = 0)
    return round(100 / umur, 2)


if __name__ == "__main__":
    daftar_tahun = [2004, 2026]
    for tahun in daftar_tahun:
        umur = hitung_umur(tahun)
        indeks = indeks_generasi(tahun)
        print(f"[v2.0] Tahun lahir: {tahun} -> Umur: {umur} tahun (Indeks: {indeks})")