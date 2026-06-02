# Product Requirement Document (PRD) - Jasa Service Scanner Fujitsu

Dokumen ini mendefinisikan persyaratan fungsional, arsitektur sistem, dan spesifikasi komponen untuk pengembangan website **Jasa Service Scanner Fujitsu** menggunakan Nuxt 3 (stable) dan Tailwind CSS.

---

## 1. Lingkup Proyek & Deskripsi Halaman
Website ini ditujukan sebagai profil bisnis, katalog spare part, dan pusat perbaikan resmi bagi korporasi & instansi pemerintahan yang menggunakan Scanner Fujitsu. Website terdiri dari 7 halaman utama:

### 1.1 Halaman Utama (Home)
- **Tujuan:** Membangun kredibilitas (15+ tahun pengalaman) dan konversi cepat (CTA WhatsApp & Konsultasi gratis).
- **Elemen Penting:**
  - Hero banner dengan latar belakang gambar sensor scanner teknis (grayscale/opacity rendah) dan gambar teknisi berpresisi tinggi.
  - Floating Stat Card (misal: "99.8% Akurasi Perbaikan").
  - Bento grid untuk penentu nilai jual (*Unique Selling Points*): Berpengalaman, Garansi Suku Cadang, Teknisi Bersertifikat.
  - Ringkasan Layanan Spesialis (Comprehensive Repair & Original Spare Parts).
  - Logo grid klien/mitra instansi pemerintah & korporat.
  - Testimoni slider/carousel dari IT Manager klien.
  - Section Ajakan Bertindak (CTA) utama terintegrasi ke WhatsApp.

### 1.2 Layanan (Services)
- **Tujuan:** Menjelaskan detail jenis perbaikan dan paket perawatan scanner.
- **Elemen Penting:**
  - List detail tipe scanner yang didukung (fi series, ScanSnap, SP series).
  - Deskripsi detail alur servis (Diagnosa awal -> Penawaran -> Perbaikan -> Quality Control -> Pengiriman kembali).
  - Fitur request *On-site Service* (layanan perbaikan di tempat kantor klien).

### 1.3 Katalog Spare Part
- **Tujuan:** Menampilkan ketersediaan suku cadang original Fujitsu untuk meyakinkan pelanggan.
- **Elemen Penting:**
  - Grid item spare part (misal: Pick Roller, Pad Assembly, Brake Roller, ADF Glass, CIS Sensor).
  - Filter pencarian berdasarkan seri scanner.
  - Tombol CTA "Tanya Stok via WhatsApp" pada setiap detail item.

### 1.4 Tentang Kami (About Us)
- **Tujuan:** Menampilkan visi, misi, legalitas usaha, dan profil tim ahli.
- **Elemen Penting:**
  - Cerita perjalanan perusahaan (Timeline 15 tahun berkarya).
  - Visi & Misi yang menekankan komitmen kualitas industrial.
  - Dokumentasi workshop, lab perbaikan yang steril, dan sertifikasi keahlian.

### 1.5 Portofolio & Klien
- **Tujuan:** Bukti kerja nyata perbaikan skala besar di berbagai instansi.
- **Elemen Penting:**
  - Galeri proyek perbaikan (sebelum vs sesudah kalibrasi scanner).
  - Studi kasus proyek (misal: Digitalisasi Arsip 10.000 Dokumen di Instansi X dengan Scanner Fujitsu yang telah dirawat).

### 1.6 Tips & Edukasi (Blog)
- **Tujuan:** Edukasi pencegahan kerusakan ringan (maintenance mandiri) sekaligus SEO organik.
- **Elemen Penting:**
  - Daftar artikel/tutorial (contoh: "Cara Membersihkan Roller Scanner Fujitsu yang Benar", "Mengatasi Error Double Feed").
  - Fitur filter kategori artikel.

### 1.7 Kontak & Formulir Booking
- **Tujuan:** Mengakomodasi permintaan servis non-WhatsApp melalui formulir formal.
- **Elemen Penting:**
  - Formulir Booking Servis (Nama, Perusahaan, Tipe Scanner, Gejala Kerusakan, Opsi Servis: Kirim/On-site).
  - Peta lokasi workshop fisik.
  - Informasi kontak resmi (telepon, email, WhatsApp).

---

## 2. Arsitektur Komponen (Menghindari Kode Duplikat)
Agar kode tetap bersih (*clean code*) dan mudah dikelola, website dirancang menggunakan struktur komponen modular Nuxt 3 yang dapat digunakan kembali (*reusable components*):

```
components/
├── global/
│   ├── MainHeader.vue           # Navbar dengan Glassmorphism
│   └── MainFooter.vue           # Footer dengan peta & informasi kontak
├── ui/
│   ├── BaseButton.vue           # Tombol serbaguna (Primary, Secondary, WA style)
│   ├── BaseCard.vue             # Card dasar untuk list layanan/testimoni/tips
│   ├── SectionHeader.vue        # Header judul section konsisten dengan garis merah
│   └── FormInput.vue            # Reusable input field dengan penanganan error state
├── sections/
│   ├── HeroSection.vue          # Hero banner utama
│   ├── BentoUSP.vue             # Bento grid keunggulan layanan
│   ├── ServiceList.vue          # Daftar ringkasan layanan
│   └── LogoGrid.vue             # Logo klien grayscale
└── features/
    ├── BookingForm.vue          # Form perbaikan terintegrasi dengan Vuelidate
    └── SparePartGrid.vue        # Grid spare part dengan filter dinamis
```

---

## 3. Validasi Form (Vuelidate)
Untuk formulir pada halaman **Kontak & Booking Servis**:
- **Paket yang Digunakan:** `@vuelidate/core` dan `@vuelidate/validators`.
- **Aturan Validasi:**
  - **Nama Lengkap:** Wajib diisi (`required`), minimal 3 karakter.
  - **Nama Instansi/Perusahaan:** Wajib diisi (`required`) untuk keperluan invoicing korporat.
  - **Email Kantor:** Format email valid (`email`), wajib diisi.
  - **No. WhatsApp/Telepon:** Wajib diisi, hanya angka (`numeric`), panjang 9-14 digit.
  - **Tipe Scanner & Masalah:** Dropdown pilihan wajib dipilih dan text area deskripsi masalah minimal 10 karakter.
- **UX Form:**
  - Elemen input berubah warna border menjadi hijau lembut (`border-emerald-500`) jika input valid (`$dirty && !$invalid`).
  - Elemen input berubah menjadi merah lembut (`border-red-500`) dan menampilkan pesan error khusus di bawah field jika input tidak valid setelah disentuh.
  - Tombol submit dinonaktifkan (`disabled`) atau memicu getaran mikro jika form belum valid sepenuhnya.

---

## 4. Animasi & Interaksi Pengguna (Smooth Animations)
Integrasi animasi menggunakan **Tailwind Transitions** dan **Nuxt Page Transitions**:

- **Page Transitions:** Transisi perpindahan halaman halus menggunakan `page-fade` (memudar) bawaan Nuxt.
- **Scroll-driven animations:** Efek *fade-in slide-up* saat elemen memasuki viewport menggunakan interaksi custom directive (atau plugin animasi seperti GSAP/Motion One jika diperlukan, namun Tailwind standard transitions diutamakan agar build tetap ringan).
- **Hover Micro-interactions:**
  - Tombol CTA: Skala membesar 1.02x (`hover:scale-105 transition-all duration-300`).
  - Cards: Mengambang ke atas (`hover:-translate-y-1 hover:shadow-2xl transition-all duration-300`).
  - Gambar Hero: Gambar scanner utama memiliki rotasi miring 3 derajat (`rotate-3`) secara default, dan bertransisi mulus ke sudut tegak (`rotate-0`) saat mouse mendekat.

---

## 5. Persyaratan Non-Fungsional & SEO
- **Framework:** Nuxt 3 (SSR aktif untuk optimasi SEO).
- **Styling:** Tailwind CSS (desain responsif mobile-first).
- **SEO Tags:** Headings terstruktur (`<h1>` tunggal per halaman), meta description dinamis menggunakan `useSeoMeta()`.
- **Accessibility:** Kontras warna teks (`on-surface` `#1A1C1C` di atas `surface` `#F9F9F9`) memenuhi standar kontras WCAG AA.
