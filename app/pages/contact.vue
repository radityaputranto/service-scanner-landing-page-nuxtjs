<script setup>
import { reactive, ref } from 'vue'
import { useVuelidate } from '@vuelidate/core'
import { required, minLength, numeric } from '@vuelidate/validators'

const formData = reactive({
  name: '',
  company: '',
  phone: '',
  deviceModel: '',
  description: ''
})

const rules = {
  name: { required },
  company: { required },
  phone: { required, numeric, minLength: minLength(9) },
  deviceModel: { required },
  description: { required, minLength: minLength(10) }
}

const v$ = useVuelidate(rules, formData)
const isSubmitted = ref(false)
const submitSuccess = ref(false)

const submitForm = async () => {
  isSubmitted.value = true
  const result = await v$.value.$validate()
  if (result) {
    submitSuccess.value = true
    setTimeout(() => { submitSuccess.value = false }, 5000)
    formData.name = ''
    formData.company = ''
    formData.phone = ''
    formData.deviceModel = ''
    formData.description = ''
    v$.value.$reset()
    isSubmitted.value = false
  }
}
</script>

<template>
<main class="pt-32 pb-24">
<!-- Hero Section Asymmetry -->
<section class="max-w-7xl mx-auto px-8 mb-20 grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
<div class="order-2 lg:order-1">
<h1 class="text-5xl lg:text-6xl font-extrabold tracking-tighter text-primary mb-6 leading-tight">
                    Presisi dalam <br/>Setiap Hubungan.
                </h1>
<p class="text-on-surface-variant text-lg max-w-md leading-relaxed mb-8">
                    Hubungi pusat solusi teknis resmi kami untuk pemeliharaan infrastruktur dan perbaikan perangkat Fujitsu dengan standar industri tertinggi.
                </p>
<div class="flex flex-wrap gap-4">
<div class="bg-surface-container-low p-4 rounded flex items-center gap-3">
<span class="material-symbols-outlined text-primary" data-icon="verified_user">verified_user</span>
<span class="text-sm font-semibold">Layanan Bersertifikat</span>
</div>
<div class="bg-surface-container-low p-4 rounded flex items-center gap-3">
<span class="material-symbols-outlined text-primary" data-icon="speed">speed</span>
<span class="text-sm font-semibold">Respon Cepat</span>
</div>
</div>
</div>
<div class="order-1 lg:order-2 relative h-[400px] lg:h-[500px]">
<img class="w-full h-full object-cover rounded-xl shadow-2xl grayscale hover:grayscale-0 transition-all duration-700" data-alt="Close-up of a professional technician working on a complex high-tech circuit board with precision tools in a clean laboratory environment" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCfM2F5XYluTaaIJgNBGXeBvz8ykfGnCgVwWT1mvNsmf5g5ISIBcp4suGUSiaA6yGAhspKu16_1eLAKkZ8PnGFD06ylWgiXjE482OjL2acbEiybS0JbMB-WSK7Hu46A0V1FuVO58CdwVkJLAspV1sJyI_dapxvNK5nan3bQx_LclFOG5ejN9ZiUjk4Pt4fVskOU6kD21jH7IItq5oRUMXzbC-rubOWXpUowAYnU7HzSyfFZZGLoJQZ_bmFzSYAd0qZhrbI2k2oVymgB"/>
<div class="absolute -bottom-6 -left-6 bg-primary-container text-on-primary p-8 rounded-lg shadow-xl hidden md:block max-w-xs">
<p class="text-sm uppercase tracking-widest mb-2 opacity-80">Jam Operasional</p>
<p class="text-xl font-bold">Senin - Sabtu</p>
<p class="text-2xl font-extrabold">09:00 - 17:00</p>
</div>
</div>
</section>
<!-- Main Content Grid -->
<section class="max-w-7xl mx-auto px-8">
<div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
<!-- Contact Form: The "Precision Tap" Form -->
<div class="lg:col-span-7 bg-surface-container-lowest p-10 rounded-xl shadow-[0_32px_32px_-12px_rgba(26,28,28,0.06)]">
<h2 class="text-3xl font-bold mb-8 flex items-center gap-3">
<span class="material-symbols-outlined text-primary" data-icon="edit_note">edit_note</span>
                        Formulir Layanan
                    </h2>
<form class="space-y-6" @submit.prevent="submitForm">
<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
<div class="space-y-2">
<label class="block text-sm font-semibold text-on-surface">Nama Lengkap</label>
<input class="w-full bg-surface-container border-none p-4 rounded focus:ring-1 focus:ring-primary/40 transition-all outline-none" placeholder="John Doe" type="text"/>
</div>
<div class="space-y-2">
<label class="block text-sm font-semibold text-on-surface">Perusahaan / Institusi</label>
<input class="w-full bg-surface-container border-none p-4 rounded focus:ring-1 focus:ring-primary/40 transition-all outline-none" placeholder="PT. Teknologi Maju" type="text"/>
</div>
</div>
<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
<div class="space-y-2">
<label class="block text-sm font-semibold text-on-surface">Nomor Telepon</label>
<input class="w-full bg-surface-container border-none p-4 rounded focus:ring-1 focus:ring-primary/40 transition-all outline-none" placeholder="+62 812 3456 7890" type="tel"/>
</div>
<div class="space-y-2">
<label class="block text-sm font-semibold text-on-surface">Model Perangkat</label>
<input class="w-full bg-surface-container border-none p-4 rounded focus:ring-1 focus:ring-primary/40 transition-all outline-none" placeholder="Contoh: ScanSnap iX1600" type="text"/>
</div>
</div>
<div class="space-y-2">
<label class="block text-sm font-semibold text-on-surface">Deskripsi Masalah</label>
<textarea class="w-full bg-surface-container border-none p-4 rounded focus:ring-1 focus:ring-primary/40 transition-all outline-none" placeholder="Jelaskan kendala teknis Anda secara mendalam..." rows="4"></textarea>
</div>
<div v-if="submitSuccess" class="bg-green-100 text-green-800 p-4 rounded text-sm font-semibold mb-4">
Permintaan perbaikan berhasil dikirim. Tim kami akan segera menghubungi Anda.
</div>
<button class="w-full bg-primary-container text-on-primary py-4 rounded-lg font-bold text-lg hover:bg-primary transition-all flex justify-center items-center gap-2 group" type="submit">
                            Kirim Permintaan Perbaikan
                            <span class="material-symbols-outlined group-hover:translate-x-1 transition-transform" data-icon="arrow_forward">arrow_forward</span>
</button>
</form>
</div>
<!-- Info Column -->
<div class="lg:col-span-5 space-y-8">
<!-- Quick Connect Card -->
<div class="bg-primary text-on-primary p-8 rounded-xl relative overflow-hidden group">
<div class="relative z-10">
<h3 class="text-2xl font-bold mb-6">Koneksi Langsung</h3>
<div class="space-y-6">
<a class="flex items-center gap-4 group/item" href="https://wa.me/62811334285?text=Halo,%20saya%20ingin%20menanyakan%20informasi%20tentang%20service%20scanner%20Fujitsu%20dengan%20tipe%20...">
<div class="w-12 h-12 bg-white/20 rounded-full flex items-center justify-center backdrop-blur-md group-hover/item:bg-white/40 transition-colors">
<span class="material-symbols-outlined" data-icon="chat" style="font-variation-settings: 'FILL' 1;">chat</span>
</div>
<div>
<p class="text-xs opacity-70 uppercase tracking-tighter">WhatsApp Support</p>
<p class="text-lg font-semibold">(+62) 811-334-285</p>
</div>
</a>
<a class="flex items-center gap-4 group/item" href="tel:+62811334285">
<div class="w-12 h-12 bg-white/20 rounded-full flex items-center justify-center backdrop-blur-md group-hover/item:bg-white/40 transition-colors">
<span class="material-symbols-outlined" data-icon="call" style="font-variation-settings: 'FILL' 1;">call</span>
</div>
<div>
<p class="text-xs opacity-70 uppercase tracking-tighter">Hotline Kantor</p>
<p class="text-lg font-semibold">(+62) 811-334-285</p>
</div>
</a>
<a class="flex items-center gap-4 group/item" href="mailto:support@industrial-atelier.id">
<div class="w-12 h-12 bg-white/20 rounded-full flex items-center justify-center backdrop-blur-md group-hover/item:bg-white/40 transition-colors">
<span class="material-symbols-outlined" data-icon="mail" style="font-variation-settings: 'FILL' 1;">mail</span>
</div>
<div>
<p class="text-xs opacity-70 uppercase tracking-tighter">Email Support</p>
<p class="text-lg font-semibold">support@fujitsu-repair.id</p>
</div>
</a>
</div>
</div>
<!-- Background Texture -->
<div class="absolute top-0 right-0 w-32 h-32 bg-white/5 rounded-full -mr-16 -mt-16 blur-2xl"></div>
</div>
<!-- Location Card -->
<div class="bg-surface-container-low p-8 rounded-xl border border-outline-variant/10">
<h3 class="text-xl font-bold mb-4 flex items-center gap-2">
<span class="material-symbols-outlined text-primary" data-icon="location_on">location_on</span>
                            Workshop Utama
                        </h3>
<p class="text-on-surface-variant mb-6 leading-relaxed">
                            Industrial Atelier Complex, <br/>
                            Jl. Engineering Raya No. 42, <br/>
                            Jakarta Selatan, DKI Jakarta 12345
                        </p>
<div class="w-full h-48 rounded-lg overflow-hidden grayscale hover:grayscale-0 transition-all duration-500">
<img class="w-full h-full object-cover" data-alt="Professional architectural map view of a central business district with minimalist clean line graphics" data-location="Jakarta" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCFJY_FxYsjwg2DHkZ8hjQHRUxhffuuOSHsuqMn3YIMrZ1gA4xO3Dk3pUM3QED1B0flLe0HLL0SFSNERQWRO-QrJnEsKQbt619qjURN5OJ3sBdbLu7tFP9V6Z__bZuPV0wAA_P_9Zn7qq6bQzCsqRhdfuVCWNSfxiPsE1uRmQnG5Ul4YVXvl4y7-tBMIDGtWwxKMhogn_qvOYE6bkNjRlrNDq8sazS9Rs-oJb5yLLlQ03GIshIjqeuVIiGi3dYkdql3-iiSGn7ZF5lg"/>
</div>
</div>
</div>
</div>
</section>
<!-- Client Logos / Trust (Monochromatic Rule) -->
<section class="max-w-7xl mx-auto px-8 mt-24">
<p class="text-center text-xs font-bold uppercase tracking-[0.2em] text-secondary/60 mb-8">Dipercaya Oleh Institusi Global</p>
<div class="flex flex-wrap justify-center items-center gap-12 lg:gap-24 opacity-40 hover:opacity-100 transition-opacity duration-500">
<span class="text-2xl font-bold font-headline grayscale">BUMN</span>
<span class="text-2xl font-bold font-headline grayscale">GOV.ID</span>
<span class="text-2xl font-bold font-headline grayscale">BANKING</span>
<span class="text-2xl font-bold font-headline grayscale">LOGISTIC</span>
<span class="text-2xl font-bold font-headline grayscale">TELECOM</span>
</div>
</section>
</main>
</template>