# kargoApp-backend

Projeyi çalıştırmak için öncelikle projeyi klonlayın.
Sonrasında gerekli kütüphanleri yükleme için requirements.txt dosyasını kullanın.
## API
### Sınıflar
- Adresler
- Alıcı Bilgileri
- Gönderici Bilgileri
- Şube Bilgileri
- Kargo Bilgileri
- Kargo
- il
- ilçe
### Adresler
Adresler API
#### GET /adres
Tüm adresleri getirir.
##### Örnek
```json
[
    {
        "id": 1,
        "adres": "adres1",
        "il": "il1",
        "ilce": "ilce1",
        "posta_kodu": "posta_kodu1"
    },
    {
        "id": 2,
        "adres": "adres2",
        "il": "il2",
        "ilce": "ilce2",
        "posta_kodu": "posta_kodu2"
    }
]
```
#### GET /adres/{id}
Belirtilen id'ye sahip adresi getirir.
##### Örnek
```json
{
    "id": 1,
    "adres_turu": "ev-iş vb..",
    "adres": "adres1",
    "ilId": "il1",
    "ilceId": "ilce1"
}
```
#### POST /adres
Yeni adres ekler.
##### Örnek
```json
{
    "adres_turu": "ev-iş vb..",
    "adres": "adres1",
    "ilId": "il1",
    "ilceId": "ilce1"
}
```
#### PUT /adres/{id}
Belirtilen id'ye sahip adresi günceller.
##### Örnek
```json
{
    "adres_turu": "ev-iş vb..",
    "adres": "adres1",
    "ilId": "il1",
    "ilceId": "ilce1"
}
```
#### DELETE /adres/{id}
Belirtilen id'ye sahip adresi siler.
### Alıcı Bilgileri
Alıcı Bilgileri API
#### GET /aliciBilgileri
Tüm alıcı bilgilerini getirir.
##### Örnek
```json
[
    {
        "id": 1,
        "ad": "ad1",
        "soyad": "soyad1",
        "telNo": "telefon1",
        "adres_id": 1,
        "tcKimlik": "tcKimlik1",
        "email": "email1"
    },
    {
        "id": 2,
        "ad": "ad2",
        "soyad": "soyad2",
        "telNo": "telefon2",
        "adres_id": 2,
        "tcKimlik": "tcKimlik2",
        "email": "email2"
    }
]
```
#### GET /aliciBilgileri/{id}
Belirtilen id'ye sahip alıcı bilgilerini getirir.
##### Örnek
```json
{
    "id": 1,
    "ad": "ad1",
    "soyad": "soyad1",
    "telNo": "telefon1",
    "adres_id": 1,
    "tcKimlik": "tcKimlik1",
    "email": "email1"
}
```
#### POST /aliciBilgileri
Yeni alıcı bilgisi ekler.
##### Örnek
```json
{
    "ad": "ad1",
    "soyad": "soyad1",
    "telNo": "telefon1",
    "adres_id": 1,
    "tcKimlik": "tcKimlik1",
    "email": "email1"
}
```
#### PUT /aliciBilgileri/{id}
Belirtilen id'ye sahip alıcı bilgilerini günceller.
##### Örnek
```json
{
    "ad": "ad1",
    "soyad": "soyad1",
    "telNo": "telefon1",
    "adres_id": 1,
    "tcKimlik": "tcKimlik1",
    "email": "email1"
}
```
#### DELETE /aliciBilgileri/{id}
Belirtilen id'ye sahip alıcı bilgilerini siler.
### Gönderici Bilgileri
Gönderici Bilgileri API
#### GET /gondericiBilgileri
Tüm gönderici bilgilerini getirir.
##### Örnek
```json
[
    {
        "id": 1,
        "ad": "ad1",
        "soyad": "soyad1",
        "telNo": "telefon1",
        "adres_id": 1,
        "tcKimlik": "tcKimlik1",
        "email": "email1"
    },
    {
        "id": 2,
        "ad": "ad2",
        "soyad": "soyad2",
        "telNo": "telefon2",
        "adres_id": 2,
        "tcKimlik": "tcKimlik2",
        "email": "email2"
    }
]
```
#### GET /gondericiBilgileri/{id}
Belirtilen id'ye sahip gönderici bilgilerini getirir.
##### Örnek
```json
{
    "id": 1,
    "ad": "ad1",
    "soyad": "soyad1",
    "telNo": "telefon1",
    "adres_id": 1,
    "tcKimlik": "tcKimlik1",
    "email": "email1"
}
```
#### POST /gondericiBilgileri
Yeni gönderici bilgisi ekler.
##### Örnek
```json
{
    "ad": "ad1",
    "soyad": "soyad1",
    "telNo": "telefon1",
    "adres_id": 1,
    "tcKimlik": "tcKimlik1",
    "email": "email1"
}
```
#### PUT /gondericiBilgileri/{id}
Belirtilen id'ye sahip gönderici bilgilerini günceller.
##### Örnek
```json
{
    "ad": "ad1",
    "soyad": "soyad1",
    "telNo": "telefon1",
    "adres_id": 1,
    "tcKimlik": "tcKimlik1",
    "email": "email1"
}
```
#### DELETE /gondericiBilgileri/{id}
Belirtilen id'ye sahip gönderici bilgilerini siler.
### İlçe
İlçe API
#### GET /ilce
Tüm ilçeleri getirir.
##### Örnek
```json
[
    {
        "id": 1,
        "ilceadi": "ilce1",
        "sehirid": 1
    },
    {
        "id": 2,
        "ilceadi": "ilce2",
        "sehirid": 2
    }
]
```
#### GET /ilce/{id}
Belirtilen id'ye sahip ilçeyi getirir.
##### Örnek
```json
{
    "id": 1,
    "ilceadi": "ilce1",
    "sehirid": 1
}
```
#### POST /ilce
Yeni ilçe ekler.
##### Örnek
```json
{
    "ilceadi": "ilce1",
    "sehirid": 1
}
```
#### PUT /ilce/{id}
Belirtilen id'ye sahip ilçeyi günceller.
##### Örnek
```json
{
    "ilceadi": "ilce1",
    "sehirid": 1
}
```
#### DELETE /ilce/{id}
Belirtilen id'ye sahip ilçeyi siler.
### İl
İl API
#### GET /il
Tüm illeri getirir.
##### Örnek
```json
[
    {
        "id": 1,
        "ilAdi": "il1"
    },
    {
        "id": 2,
        "ilAdi": "il2"
    }
]
```
#### GET /il/{id}
Belirtilen id'ye sahip illeri getirir.
##### Örnek
```json
{
    "id": 1,
    "ilAdi": "il1"
}
```
#### POST /il
Yeni il ekler.
##### Örnek
```json
{
    "ilAdi": "il1"
}
```
#### PUT /il/{id}
Belirtilen id'ye sahip ili günceller.
##### Örnek
```json
{
    "ilAdi": "il1"
}
```
#### DELETE /il/{id}
Belirtilen id'ye sahip ili siler.
### Kargo
Kargo API
#### GET /kargo
Tüm kargoları getirir.
##### Örnek
```json
[
    {
        "id": 1,
        "kargoAdi":"kargo1",
        "adet": 1,
        "yukseklik": 1,
        "genislik": 1,
        "kirilma": "kirilir"
    },
    {
        "id": 2,
        "kargoAdi":"kargo2",
        "adet": 2,
        "yukseklik": 2,
        "genislik": 2,
        "kirilma": "kirilir"
    }
]
```
#### GET /kargo/{id}
Belirtilen id'ye sahip kargoyu getirir.
##### Örnek
```json
{
    "id": 1,
    "kargoAdi":"kargo1",
    "adet": 1,
    "yukseklik": 1,
    "genislik": 1,
    "kirilma": "kirilir"
}
```
#### POST /kargo
Yeni kargo ekler.
##### Örnek
```json
{
    "kargoAdi":"kargo1",
    "adet": 1,
    "yukseklik": 1,
    "genislik": 1,
    "kirilma": "kirilir"
}
```
#### PUT /kargo/{id}
Belirtilen id'ye sahip kargoyu günceller.
##### Örnek
```json
{
    "kargoAdi":"kargo1",
    "adet": 1,
    "yukseklik": 1,
    "genislik": 1,
    "kirilma": "kirilir"
}
```
#### DELETE /kargo/{id}
Belirtilen id'ye sahip kargoyu siler.
###
### Kargo Bilgileri
Kargo Bilgileri API
#### GET /kargoBilgileri
Tüm kargo bilgilerini getirir.
##### Örnek
```json
[
    {
        "id": 1,
        "gondericiId": 1,
        "aliciId": 1,
        "kargoId": 1,
        "subeId":1,
        "kargo_tarihi": "2020-01-01",
        "kargo_odemeTuru": "gönderici ödemeli",
    }
]
```
#### GET /kargoBilgileri/{id}
Belirtilen id'ye sahip kargo bilgilerini getirir.
##### Örnek
```json
{
    "id": 1,
    "gondericiId": 1,
    "aliciId": 1,
    "kargoId": 1,
    "subeId":1,
    "kargo_tarihi": "2020-01-01",
    "kargo_odemeTuru": "gönderici ödemeli",
}
```
#### POST /kargoBilgileri
Yeni kargo bilgisi ekler.
##### Örnek
```json
{
    "gondericiId": 1,
    "aliciId": 1,
    "kargoId": 1,
    "subeId":1,
    "kargo_tarihi": "2020-01-01",
    "kargo_odemeTuru": "gönderici ödemeli",
}
```
#### PUT /kargoBilgileri/{id}
Belirtilen id'ye sahip kargo bilgisini günceller.
##### Örnek
```json
{
    "gondericiId": 1,
    "aliciId": 1,
    "kargoId": 1,
    "subeId":1,
    "kargo_tarihi": "2020-01-01",
    "kargo_odemeTuru": "gönderici ödemeli",
}
```
#### DELETE /kargoBilgileri/{id}
Belirtilen id'ye sahip kargo bilgisini siler.
### Sube Bilgileri
Sube Bilgileri API
#### GET /subeBilgileri
Tüm şube bilgilerini getirir.
##### Örnek
```json
[
    {
        "id": 1,
        "ad": "ad1",
        "adres_id": "adres1",
        "telNo": "telefon1",
        "sube_yetkilisi": "yetkili1"
    }
]
```
#### GET /subeBilgileri/{id}
Belirtilen id'ye sahip şube bilgilerini getirir.
##### Örnek
```json
{
    "id": 1,
    "ad": "ad1",
    "adres_id": "adres1",
    "telNo": "telefon1",
    "sube_yetkilisi": "yetkili1"
}
```
#### POST /subeBilgileri
Yeni şube bilgisi ekler.
##### Örnek
```json
{
    "ad": "ad1",
    "adres_id": "adres1",
    "telNo": "telefon1",
    "sube_yetkilisi": "yetkili1"
}
```
#### PUT /subeBilgileri/{id}
Belirtilen id'ye sahip şube bilgisini günceller.
##### Örnek
```json
{
    "ad": "ad1",
    "adres_id": "adres1",
    "telNo": "telefon1",
    "sube_yetkilisi": "yetkili1"
}
```
#### DELETE /subeBilgileri/{id}
Belirtilen id'ye sahip şube bilgisini siler.




