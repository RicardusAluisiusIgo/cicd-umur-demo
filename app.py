from datetime import datetime


def hitung_umur(tahun_lahir: int, tahun_sekarang: int = None) -> int:
    if tahun_sekarang is None:
        tahun_sekarang = datetime.now().year
    return tahun_sekarang - tahun_lahir


if __name__ == "__main__":
    daftar_tahun = [2004, 2026]
    for tahun in daftar_tahun:
        umur = hitung_umur(tahun)
        print(f"[v1.0] Tahun lahir: {tahun} -> Umur: {umur} tahun")