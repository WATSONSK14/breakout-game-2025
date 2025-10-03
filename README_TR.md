# 🎮 Breakout Game 2025

[![Lisans: MIT](https://img.shields.io/badge/Lisans-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Turtle](https://img.shields.io/badge/Grafik-Turtle-green.svg)](https://docs.python.org/3/library/turtle.html)

Python Turtle grafikleri ile geliştirilmiş klasik Breakout arcade oyununun modern bir uygulaması. Sürükleyici ses efektleri, progresif zorluk skalası ve akıcı oyun mekanikleri ile zamansız paddle-ve-top deneyimini çağdaş bir cilayla hayata geçiriyor.

## 🎯 Özellikler

- **Klasik Breakout Oynanışı**: Zıplayan top ve paddle ile renkli blokları kırın
- **Progresif Zorluk**: Daha fazla blok yok ettikçe top hızı artar
- **Ses Efektleri**: Tüm oyun aksiyonları için sürükleyici ses geri bildirimi
- **Skor Sistemi**: Blok renklerine göre puan kazanın (blok başına 7-3 puan)
- **Yaşam Sistemi**: Görsel kalp göstergeleri ile 3 can
- **Özel Efektler**: Kırmızı bloklar paddle'ınızı küçültür ve top hızını artırır
- **Modern Arayüz**: Retro stile sahip temiz, koyu temalı arayüz
- **Çoklu Platform**: Windows, macOS ve Linux'ta çalışır

## 🎮 Nasıl Oynanır

### Kontroller
- **Sol Fare Tıklaması**: Oyunu başlat
- **Ok Tuşları**: Paddle'ı sola/sağa hareket ettir
- **Boşluk Çubuğu**: Oyun bittikten sonra oyunu yeniden başlat

### Oyun Kuralları
1. **Amaç**: Topunuzu paddle ile zıplatarak tüm renkli blokları yok edin
2. **Yaşamlar**: 3 canla (kalp) başlarsınız. Top paddle'ın altına düştüğünde can kaybedersiniz
3. **Puanlama**: Farklı renkli bloklar farklı puanlar verir:
   - 🔴 **Kırmızı bloklar**: 7 puan (paddle'ı küçültür ve topu hızlandırır)
   - 🟠 **Turuncu bloklar**: 5 puan
   - 🟢 **Yeşil bloklar**: 3 puan
   - 🟡 **Sarı bloklar**: 3 puan
4. **Progresif Zorluk**: Her blok yok edildiğinde top hızı artar
5. **Zafer**: Tüm blokları yok ederek kazanın
6. **Yenilgi**: 3 canınızı da kaybedin

### Özel Mekanikler
- **Kırmızı Blok Efekti**: Kırmızı blok vurduğunuzda paddle'ınız yarı boyuta küçülür ve top hızlanır
- **Top Fiziği**: Top duvarlardan, bloklardan ve paddle'dan gerçekçi şekilde seker
- **Hız Ölçeklendirme**: İlerledikçe oyun daha zorlaşır

## 🚀 Kurulum

### Gereksinimler
- Python 3.6 veya üzeri
- Ses efektleri için pygame kütüphanesi

### Kurulum
1. **Depoyu klonlayın**:
   ```bash
   git clone https://github.com/yourusername/breakout-game-2025.git
   cd breakout-game-2025
   ```

2. **Bağımlılıkları yükleyin**:
   ```bash
   pip install pygame
   ```

3. **Oyunu çalıştırın**:
   ```bash
   python main.py
   ```

### Alternatif: Çalıştırılabilir Versiyon
Python kurulumu yapmadan anında oyun oynamak için:
- Depodan `main.exe` dosyasını indirin
- Çalıştırmak için çift tıklayın (sadece Windows)
- Ek bağımlılık gerekmez

## 📁 Proje Yapısı

```
breakout-game-2025/
├── main.py              # Ana oyun giriş noktası ve oyun döngüsü
├── game_utils.py        # Temel oyun mantığı ve yardımcı fonksiyonlar
├── ball.py              # Top fiziği ve hareket
├── paddle.py            # Paddle kontrolleri ve hareket
├── wall_utils.py        # Duvar ve blok oluşturma
├── icon.ico             # Oyun simgesi
├── main.exe             # Bağımsız çalıştırılabilir (Windows)
├── main.spec            # PyInstaller yapılandırması
├── sound/               # Ses varlıkları
│   ├── block.mp3        # Blok yok etme sesi
│   ├── game_over.mp3    # Oyun bitti sesi
│   ├── heart.mp3        # Yaşam kaybetme sesi
│   ├── paddle.mp3       # Paddle vuruş sesi
│   └── win.mp3          # Zafer sesi
├── README.md            # İngilizce dokümantasyon
└── README_TR.md         # Bu dosya (Türkçe)
```

## 🔧 Teknik Detaylar

### Mimari
- **Nesne Yönelimli Tasarım**: Ball, Paddle, Wall ve GameUtils için modüler sınıflar
- **Olay Güdümlü**: Fare tıklamaları ve klavye girişleri oyun akışını kontrol eder
- **Çarpışma Algılama**: Top-paddle ve top-blok etkileşimleri için hassas vuruş algılama
- **Durum Yönetimi**: Oyun durumları (oyun, duraklatılmış, oyun bitti) düzgün yönetilir

### Ana Bileşenler
- **Game Sınıfı**: Ana oyun kontrolcüsü ve olay işleyicisi
- **GameUtils Sınıfı**: Temel oyun mekanikleri, puanlama ve ses yönetimi
- **Ball Sınıfı**: Fizik simülasyonu ve hareket mantığı
- **Paddle Sınıfı**: Oyuncu girişi işleme ve hareket kısıtlamaları
- **Wall Sınıfı**: Blok oluşturma ve düzen yönetimi

### Performans Optimizasyonları
- **Turtle Grafikleri**: Verimli 2D grafik işleme
- **Çarpışma Optimizasyonu**: Çarpışma döngülerinden erken çıkış
- **Bellek Yönetimi**: Oyun nesnelerinin düzgün temizlenmesi

## 🎨 Özelleştirme

### Oyun Parametrelerini Değiştirme
İlgili dosyalarda bu değerleri düzenleyerek oyunu kolayca özelleştirebilirsiniz:

**Top Hızı** (`ball.py`):
```python
self.y_move = -3  # Başlangıç dikey hızı
self.x_move = 3   # Başlangıç yatay hızı
```

**Paddle Boyutu** (`paddle.py`):
```python
self.shapesize(stretch_wid=1, stretch_len=5)  # Genişlik çarpanı
```

**Blok Düzeni** (`wall_utils.py`):
```python
colors = [
    ("red", 2),    # Renk ve satır sayısı
    ("orange", 2),
    ("green", 2),
    ("yellow", 2)
]
```

### Yeni Özellikler Ekleme
- **Güçlendiriciler**: Benzersiz efektlere sahip özel bloklar
- **Seviyeler**: Artan zorlukla çoklu düzenler oluşturma
- **Yüksek Skorlar**: Kalıcı skor takibi uygulama
- **Çoklu Oyuncu**: Rekabetçi iki oyunculu mod ekleme

## 🐛 Sorun Giderme

### Yaygın Sorunlar

**Oyun başlamıyor:**
- Python 3.6+ kurulu olduğundan emin olun
- pygame'i yükleyin: `pip install pygame`
- Tüm dosyaların aynı dizinde olduğunu kontrol edin

**Ses yok:**
- pygame'in düzgün yüklendiğini doğrulayın
- `sound/` klasörünün tüm ses dosyalarıyla birlikte var olduğunu kontrol edin
- Linux'ta ek ses kütüphaneleri yüklemeniz gerekebilir

**Performans sorunları:**
- Sistem kaynaklarını serbest bırakmak için diğer uygulamaları kapatın
- Eski sistemlerde `game_loop()` içindeki bekleme süresini artırın (`main.py` 59. satır)

## 🤝 Katkıda Bulunma

Katkılarınız hoş karşılanır! İşte nasıl yardımcı olabileceğiniz:

1. **Depoyu çatallayın**
2. **Özellik dalı oluşturun**: `git checkout -b feature/harika-ozellik`
3. **Değişikliklerinizi kaydedin**: `git commit -m 'Harika bir özellik ekle'`
4. **Dalı gönderin**: `git push origin feature/harika-ozellik`
5. **Çekme İsteği açın**

### Geliştirme Kuralları
- PEP 8 stil kurallarını takip edin
- Karmaşık mantık için yorum ekleyin
- Değişikliklerinizi kapsamlı şekilde test edin
- Gerektiğinde dokümantasyonu güncelleyin

## 📝 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 🙏 Teşekkürler

- **Atari**: Orijinal Breakout oyun konseptini yarattığı için
- **Python Turtle Grafikleri**: Mükemmel 2D grafik kütüphanesi sağladığı için
- **Pygame**: Yüksek kaliteli ses efektleri sağladığı için
- **Açık Kaynak Topluluğu**: İlham ve destek için

## 📧 İletişim

- **GitHub**: [@WATSONSK14]


---

⭐ **Bu oyunu beğendiyseniz, lütfen yıldız verin!** ⭐

*Python ve Turtle Grafikleri kullanılarak ❤️ ile yapıldı*
