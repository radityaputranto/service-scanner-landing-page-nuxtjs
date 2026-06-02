<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  limit: { type: Number, default: 0 }
})

const activeFilter = ref('all')

const spareParts = [
  { id: 1, name: 'Pick Roller Set', series: 'fi-series', model: 'fi-8170 / fi-8190', price: 'Rp 1.250.000', stock: 'Tersedia', image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuDoIgOQRVoabpai4uzdpGQbhFPTJkATmFOlvFZySDCSqfd8zk9fRml5UuWLubqPxgD4tV8ZxowLXUQ9bHoojkkFTfF-5i8hkPlafqdcFDX-TJcCX-FXPQwbOcVO3VUuK_YTchMMeXwuu-MUkfVjtEwYNxljcPhKMT_kP_um6N3NurV3eAuIF8v2tYlaLQ714ZlXktB5m7taIAepcjtVur8i1vB4jP4aqa3bPSAUzIF6AXkrE3NDkMsBGAikyO2gajSwO2i4o0pPxWdp' },
  { id: 2, name: 'Brake Roller', series: 'fi-series', model: 'fi-7160 / fi-7260', price: 'Rp 850.000', stock: 'Tersedia', image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuBLUhVeS4QmYoL-YgpDnxobCB1neRY45hKLpRJOeaMR8e5t2B2Jsb0nltjCJ4ENug3Eux21Yu8JvK9uGReQdM1aJRJdUU-KVS0XiR_J2adVWu2Gn7XbmwqQcPEGAhfYlNU3GWOx0lpV_Q67R5u-w3CA2PO2Zb97ZtcjHHcZepITphrLZh1KRVPQj-n4EUBmWYG4-Ht-Ut8EPauHZqUGL2JqLQO1zE-5DvFoRCtcnS77S5OvoZlMW7LoyFJwhJoLp8JgxZpaqU6fmIqm' },
  { id: 3, name: 'Pad Assembly', series: 'scansnap', model: 'ScanSnap iX1600', price: 'Rp 450.000', stock: 'Terbatas', image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuDdYZb8HzUPK6veUXIngdzbA1h3c0pbLC5n7p5H_p31-vIFRfF200mCpefbqb4sVDCVY0MCH3DaXOoQ7X1srpQquuorNTz3sfIRZpTlba11fly-QRhe0SS0YqWNS6d_1tCmGZ4zSiEs-FqVeaqi7fREdNIclKpw4L1giJawHFF4EbAa9ZT8WuYwpo8n-af5HQvrZnxde8Hqm2CRHgfKTCXGXgkxhuVSoyaZMVoVbjHsN9RLC7iE4wHG71k7J-1Ja5bFJ1W3FXj7P3Fu' },
  { id: 4, name: 'ADF Glass', series: 'fi-series', model: 'fi-7480 / fi-7460', price: 'Rp 2.100.000', stock: 'Pre-Order', image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuBv8yydKysAPfZqUja6WlOjDwqEsJFXLGmwusk8YKIKyRdDtkpcSUkPq68m5STJxIAEwRKw-x8PGmTyfim9SRPT2TqDCSnmDuyRVZZkw35MHiU17kdo81q6Yti8xmvvNupOR7EPOV1P2rjubNpJ96CEK4jsGVWZUk_VwpSrV4FsskAvf83UxuI7IQrkJ4OelvFNzki0xNCqF-xxlYXMQMth3Kk8p1YV6ZmpmrEXC7rOgj4c8sgUXW7oy6oPjYEFIdt4y7INmbPXCp_z' },
  { id: 5, name: 'Separation Roller', series: 'sp-series', model: 'SP-1120 / SP-1130', price: 'Rp 650.000', stock: 'Tersedia', image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuDoIgOQRVoabpai4uzdpGQbhFPTJkATmFOlvFZySDCSqfd8zk9fRml5UuWLubqPxgD4tV8ZxowLXUQ9bHoojkkFTfF-5i8hkPlafqdcFDX-TJcCX-FXPQwbOcVO3VUuK_YTchMMeXwuu-MUkfVjtEwYNxljcPhKMT_kP_um6N3NurV3eAuIF8v2tYlaLQ714ZlXktB5m7taIAepcjtVur8i1vB4jP4aqa3bPSAUzIF6AXkrE3NDkMsBGAikyO2gajSwO2i4o0pPxWdp' },
  { id: 6, name: 'CIS Sensor Module', series: 'fi-series', model: 'fi-800R', price: 'Rp 3.500.000', stock: 'Pre-Order', image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuBLUhVeS4QmYoL-YgpDnxobCB1neRY45hKLpRJOeaMR8e5t2B2Jsb0nltjCJ4ENug3Eux21Yu8JvK9uGReQdM1aJRJdUU-KVS0XiR_J2adVWu2Gn7XbmwqQcPEGAhfYlNU3GWOx0lpV_Q67R5u-w3CA2PO2Zb97ZtcjHHcZepITphrLZh1KRVPQj-n4EUBmWYG4-Ht-Ut8EPauHZqUGL2JqLQO1zE-5DvFoRCtcnS77S5OvoZlMW7LoyFJwhJoLp8JgxZpaqU6fmIqm' }
]

const filteredParts = computed(() => {
  let filtered = activeFilter.value === 'all' 
    ? spareParts 
    : spareParts.filter(part => part.series === activeFilter.value)
    
  if (props.limit > 0) {
    return filtered.slice(0, props.limit)
  }
  return filtered
})
</script>

<template>
  <div>
    <!-- Filters -->
    <div class="flex flex-wrap gap-4 mb-10 justify-center">
      <button 
        @click="activeFilter = 'all'" 
        class="px-6 py-2.5 rounded-full font-bold transition-colors"
        :class="activeFilter === 'all' ? 'bg-primary text-white' : 'bg-surface-container border border-outline-variant hover:bg-surface-container-high'"
      >Semua Part</button>
      <button 
        @click="activeFilter = 'fi-series'" 
        class="px-6 py-2.5 rounded-full font-bold transition-colors"
        :class="activeFilter === 'fi-series' ? 'bg-primary text-white' : 'bg-surface-container border border-outline-variant hover:bg-surface-container-high'"
      >fi Series</button>
      <button 
        @click="activeFilter = 'scansnap'" 
        class="px-6 py-2.5 rounded-full font-bold transition-colors"
        :class="activeFilter === 'scansnap' ? 'bg-primary text-white' : 'bg-surface-container border border-outline-variant hover:bg-surface-container-high'"
      >ScanSnap</button>
      <button 
        @click="activeFilter = 'sp-series'" 
        class="px-6 py-2.5 rounded-full font-bold transition-colors"
        :class="activeFilter === 'sp-series' ? 'bg-primary text-white' : 'bg-surface-container border border-outline-variant hover:bg-surface-container-high'"
      >SP Series</button>
    </div>

    <!-- Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      <div v-for="part in filteredParts" :key="part.id" class="bg-surface-container-lowest rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 flex flex-col">
        <div class="h-48 overflow-hidden bg-surface-container relative">
          <div class="absolute top-4 right-4 z-10 px-3 py-1 rounded-full text-xs font-bold shadow-md"
               :class="{
                 'bg-emerald-100 text-emerald-800': part.stock === 'Tersedia',
                 'bg-amber-100 text-amber-800': part.stock === 'Terbatas',
                 'bg-slate-100 text-slate-800': part.stock === 'Pre-Order'
               }">
            {{ part.stock }}
          </div>
          <img :src="part.image" :alt="part.name" class="w-full h-full object-cover grayscale mix-blend-multiply opacity-80 hover:grayscale-0 hover:opacity-100 transition-all duration-500" />
        </div>
        <div class="p-6 flex-grow flex flex-col">
          <div class="text-xs font-bold text-secondary uppercase tracking-wider mb-2">{{ part.model }}</div>
          <h3 class="text-xl font-bold mb-2">{{ part.name }}</h3>
          <p class="text-on-surface-variant flex-grow mb-6">Suku cadang original Fujitsu dengan jaminan kualitas standar pabrikan.</p>
          <div class="flex items-center justify-between mt-auto">
            <span class="font-bold text-primary">{{ part.price }}</span>
            <a :href="`https://wa.me/#?text=Halo, saya ingin menanyakan ketersediaan ${part.name} untuk model ${part.model}`" class="text-sm font-bold flex items-center gap-1 hover:text-primary transition-colors">
              Tanya Stok <Icon name="material-symbols:arrow-forward" />
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
