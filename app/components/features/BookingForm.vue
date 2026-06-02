<script setup>
import { useVuelidate } from '@vuelidate/core'
import { required, email, numeric, minLength } from '@vuelidate/validators'
import { reactive, ref } from 'vue'

const formData = reactive({
  name: '',
  company: '',
  email: '',
  phone: '',
  scannerType: '',
  problem: ''
})

const rules = {
  name: { required, minLength: minLength(3) },
  company: { required },
  email: { required, email },
  phone: { required, numeric, minLength: minLength(9) },
  scannerType: { required },
  problem: { required, minLength: minLength(10) }
}

const v$ = useVuelidate(rules, formData)
const isSubmitting = ref(false)
const isSuccess = ref(false)

const submitForm = async () => {
  const isFormCorrect = await v$.value.$validate()
  if (!isFormCorrect) return
  
  isSubmitting.value = true
  
  // Simulate API call
  setTimeout(() => {
    isSubmitting.value = false
    isSuccess.value = true
    
    // Reset form after success
    setTimeout(() => {
      isSuccess.value = false
      Object.keys(formData).forEach(key => formData[key] = '')
      v$.value.$reset()
    }, 3000)
  }, 1500)
}
</script>

<template>
  <div class="bg-surface-container-lowest p-8 rounded-2xl shadow-xl max-w-2xl mx-auto w-full">
    <div v-if="isSuccess" class="text-center py-12 flex flex-col items-center justify-center">
      <div class="w-16 h-16 bg-emerald-100 text-emerald-600 rounded-full flex items-center justify-center mb-6">
        <Icon name="material-symbols:check" class="text-3xl font-bold" />
      </div>
      <h3 class="text-2xl font-bold mb-2">Permintaan Terkirim!</h3>
      <p class="text-on-surface-variant">Tim teknisi kami akan segera menghubungi Anda dalam 1x24 jam.</p>
    </div>
    
    <form v-else @submit.prevent="submitForm" class="space-y-6">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <FormInput
          id="name"
          label="Nama Lengkap"
          v-model="formData.name"
          @blur="v$.name.$touch"
          :error="v$.name.$error ? 'Nama wajib diisi (min. 3 karakter)' : ''"
          placeholder="John Doe"
        />
        
        <FormInput
          id="company"
          label="Instansi / Perusahaan"
          v-model="formData.company"
          @blur="v$.company.$touch"
          :error="v$.company.$error ? 'Nama perusahaan wajib diisi' : ''"
          placeholder="PT. Teknologi Indonesia"
        />
        
        <FormInput
          id="email"
          type="email"
          label="Email Kantor"
          v-model="formData.email"
          @blur="v$.email.$touch"
          :error="v$.email.$error ? 'Format email tidak valid' : ''"
          placeholder="john@perusahaan.com"
        />
        
        <FormInput
          id="phone"
          type="tel"
          label="No. WhatsApp / Telepon"
          v-model="formData.phone"
          @blur="v$.phone.$touch"
          :error="v$.phone.$error ? 'Nomor tidak valid (min. 9 angka)' : ''"
          placeholder="081234567890"
        />
      </div>
      
      <div class="flex flex-col gap-1.5">
        <label for="scannerType" class="text-sm font-semibold text-on-surface-variant">Tipe Scanner</label>
        <select 
          id="scannerType" 
          v-model="formData.scannerType"
          @blur="v$.scannerType.$touch"
          class="px-4 py-3 rounded-lg border bg-surface-container-lowest focus:ring-2 focus:ring-primary focus:outline-none transition-colors"
          :class="[v$.scannerType.$error ? 'border-red-500' : 'border-outline-variant']"
        >
          <option value="" disabled>Pilih Tipe Scanner</option>
          <option value="fi-series">Fujitsu fi Series (fi-8170, dll)</option>
          <option value="scansnap">Fujitsu ScanSnap</option>
          <option value="sp-series">Fujitsu SP Series</option>
          <option value="other">Lainnya / Tidak Tahu</option>
        </select>
        <span v-if="v$.scannerType.$error" class="text-xs text-red-500 mt-1 flex items-center gap-1">
          <Icon name="material-symbols:error" class="text-sm" /> Tipe scanner wajib dipilih
        </span>
      </div>
      
      <FormInput
        id="problem"
        label="Gejala Kerusakan / Masalah"
        :isTextarea="true"
        v-model="formData.problem"
        @blur="v$.problem.$touch"
        :error="v$.problem.$error ? 'Jelaskan masalah secara singkat (min. 10 karakter)' : ''"
        placeholder="Contoh: Scanner sering paper jam atau muncul garis hitam saat scan..."
      />
      
      <button 
        type="submit" 
        class="w-full bg-primary text-on-primary py-4 rounded-lg font-bold text-lg hover:bg-primary-container transition-all flex justify-center items-center gap-2"
        :disabled="isSubmitting"
        :class="{'opacity-75 cursor-not-allowed': isSubmitting}"
      >
        <Icon v-if="isSubmitting" name="material-symbols:progress-activity" class="animate-spin text-xl" />
        <Icon v-else name="material-symbols:send" class="text-xl" />
        {{ isSubmitting ? 'Mengirim...' : 'Kirim Permintaan Booking' }}
      </button>
    </form>
  </div>
</template>
