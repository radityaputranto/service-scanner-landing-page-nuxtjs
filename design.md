# Design System: Precision & Performance (The Industrial Atelier)

Dokumen ini mendefinisikan panduan visual, token desain, tipografi, dan arsitektur UI untuk proyek **Jasa Service Scanner Fujitsu** berdasarkan ekstraksi desain dari Google Stitch.

---

## 1. Konsep Kreatif (Creative North Star)
**"The Industrial Atelier"**
Konsep ini menggabungkan presisi teknis tingkat tinggi dari teknologi engineering Fujitsu dengan tata letak editorial premium bergaya majalah arsitektur.
- **Prinsip Utama:**
  - Mengutamakan *white space* (ruang bernapas) daripada garis pembatas tipis (`<hr>` atau `border-1px` untuk memisahkan bagian dilarang keras).
  - Menggunakan transisi kedalaman (tonal layering) dengan warna latar belakang yang berbeda untuk memisahkan section.
  - Memanfaatkan *asymmetry grid* dan overlap elemen (misal, gambar mesin presisi yang overlap dengan card teks melayang).
  - Sentuhan *Glassmorphic* untuk elemen melayang seperti Navbar atau Sticky CTA.

---

## 2. Palet Warna (Color System)
Sistem warna menggunakan tema monochromatic red (terinspirasi dari merah khas Fujitsu) dengan tingkat kontras yang ramah aksesibilitas (WCAG).

| Token Name | Hex Code | Deskripsi / Penggunaan |
| :--- | :--- | :--- |
| **Primary** | `#7A0011` | Warna brand utama (Command Red). Digunakan untuk teks krusial, link aktif, dan ikon utama. |
| **Primary Container** | `#9E1B23` | Warna CTA utama, background tombol primer, dan area sorotan. |
| **On-Primary** | `#FFFFFF` | Warna teks di atas background Primary / Primary Container. |
| **Background / Surface** | `#F9F9F9` | Kanvas dasar halaman (Level 0). |
| **Surface Container Low** | `#F3F3F3` | Background untuk section sekunder berukuran besar (Level 1). |
| **Surface Container Lowest** | `#FFFFFF` | Background untuk card interaktif yang melayang (Level 2). |
| **On-Surface** | `#1A1C1C` | Warna teks utama / teks body dengan kontras tinggi. |
| **On-Surface-Variant** | `#59413F` | Warna teks deskripsi / teks sekunder agar lebih hangat dan mengurangi ketegangan mata. |
| **Secondary** | `#5F5E5E` | Warna abu-abu monokromatik untuk teks pendukung atau logo klien (opacity 50%). |
| **Outline-Variant** | `#E1BFBC` | Digunakan hanya untuk *ghost borders* (border transparan 20%) pada elemen input form jika sangat dibutuhkan. |

---

## 3. Tipografi (Typography)
Menggunakan Google Fonts yang merepresentasikan presisi teknis dan keandalan korporat:

- **Headings (Display & Title):** **Manrope** (font-sans)
  - `Display 1` (Hero Headline): `text-5xl md:text-7xl font-extrabold tracking-tighter leading-[1.1]`
  - `Headline 2` (Section Title): `text-3xl md:text-5xl font-extrabold tracking-tight`
  - `Title 3` (Card Title): `text-xl md:text-2xl font-bold`
- **Body & Labels:** **Inter** (font-sans)
  - `Body Base`: `text-base text-on-surface-variant leading-relaxed`
  - `Body Large`: `text-lg text-on-surface-variant leading-relaxed`
  - `Button Text`: `text-sm font-semibold tracking-wide`

---

## 4. Sistem Layout & Spacing
- **No-Border Rule:** Dilarang menggunakan border padat untuk memisahkan section. Gunakan perbedaan warna latar belakang:
  - Latar belakang berseling antara `#F9F9F9` (Surface) dan `#F3F3F3` (Surface-Container-Low).
- **Asymmetric Grid:** Element gambar pada section besar disarankan memiliki rotasi minor (misal `rotate-3` yang berubah menjadi `rotate-0` saat di-hover) untuk memberikan kesan dinamis dan hidup.
- **Glassmorphism:** Navigation bar menggunakan background `bg-white/60` dengan filter `backdrop-blur-xl` untuk efek kaca modern.

---

## 5. Micro-Animations & Interaksi (Tailwind & CSS)
Untuk menghasilkan transisi yang premium dan halus (*smooth*):
- **Hover Transitions:** 
  - Tombol utama: transisi warna latar belakang dan pergeseran skala halus (`hover:scale-[1.02] transition-all duration-200`).
  - Link Menu: transisi perubahan warna dari abu-abu menjadi merah Fujitsu (`hover:text-primary transition-colors duration-200`).
  - Card Layanan: efek bayangan halus saat melayang (extra-diffused shadow: `hover:shadow-xl transition-shadow duration-300`).
- **Scroll Reveal (Framer Motion / Tailwind-based):**
  - Section baru memudar ke atas (*fade-in slide-up*) saat di-scroll.
- **Logo Grids:**
  - Logo klien diatur grayscale dan opacity `0.5`, bertransisi menjadi berwarna penuh dan opacity `1.0` saat di-hover.

---

## 6. Iconography
Menggunakan **Material Symbols Outlined** untuk konsistensi ikon teknis.
- Menggunakan parameter konfigurasi `font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;`.
- Ikon status aktif menggunakan `'FILL' 1` dengan warna merah utama.
