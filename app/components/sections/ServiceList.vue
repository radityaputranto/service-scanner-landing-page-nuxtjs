<template>
  <section class="py-24 bg-surface" id="services">
    <div class="max-w-7xl mx-auto px-8">
      <div class="text-center mb-16 reveal">
        <h2 class="text-3xl md:text-5xl font-extrabold tracking-tight mb-4">Layanan Spesialis Kami</h2>
        <div class="h-1.5 w-24 bg-primary mx-auto rounded-full"></div>
      </div>
      
      <div class="grid grid-cols-1 md:grid-cols-2 gap-12">
        <div class="group relative overflow-hidden rounded-xl bg-surface-container-lowest shadow-md hover:shadow-2xl transition-shadow duration-300 reveal delay-100">
          <div class="aspect-[16/9] overflow-hidden">
            <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuDoIgOQRVoabpai4uzdpGQbhFPTJkATmFOlvFZySDCSqfd8zk9fRml5UuWLubqPxgD4tV8ZxowLXUQ9bHoojkkFTfF-5i8hkPlafqdcFDX-TJcCX-FXPQwbOcVO3VUuK_YTchMMeXwuu-MUkfVjtEwYNxljcPhKMT_kP_um6N3NurV3eAuIF8v2tYlaLQ714ZlXktB5m7taIAepcjtVur8i1vB4jP4aqa3bPSAUzIF6AXkrE3NDkMsBGAikyO2gajSwO2i4o0pPxWdp" alt="Repair Service" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" />
          </div>
          <div class="p-10">
            <div class="flex justify-between items-start mb-4">
              <h3 class="text-2xl font-bold">Comprehensive Repair</h3>
              <span class="bg-primary-container/10 text-primary px-3 py-1 rounded text-xs font-bold">MOST POPULAR</span>
            </div>
            <p class="text-on-surface-variant mb-8 leading-relaxed">
              Diagnosa menyeluruh untuk masalah sensor, paper-jam kronis, hingga masalah board elektronik pada scanner seri fi, ScanSnap, dan SP.
            </p>
            <ul class="space-y-3 mb-10">
              <li class="flex items-center gap-2 text-sm text-on-surface-variant">
                <Icon name="material-symbols:check-circle" class="text-primary text-lg" />
                Cleaning & Calibration
              </li>
              <li class="flex items-center gap-2 text-sm text-on-surface-variant">
                <Icon name="material-symbols:check-circle" class="text-primary text-lg" />
                Electronic Board Repair
              </li>
            </ul>
            <NuxtLink to="/services" class="text-primary font-bold inline-flex items-center gap-2 group-hover:gap-4 transition-all">
              Pelajari Selengkapnya
              <Icon name="material-symbols:arrow-right-alt" class="text-xl" />
            </NuxtLink>
          </div>
        </div>
        
        <div class="group relative overflow-hidden rounded-xl bg-surface-container-lowest shadow-md hover:shadow-2xl transition-shadow duration-300 reveal delay-200">
          <div class="aspect-[16/9] overflow-hidden">
            <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuBLUhVeS4QmYoL-YgpDnxobCB1neRY45hKLpRJOeaMR8e5t2B2Jsb0nltjCJ4ENug3Eux21Yu8JvK9uGReQdM1aJRJdUU-KVS0XiR_J2adVWu2Gn7XbmwqQcPEGAhfYlNU3GWOx0lpV_Q67R5u-w3CA2PO2Zb97ZtcjHHcZepITphrLZh1KRVPQj-n4EUBmWYG4-Ht-Ut8EPauHZqUGL2JqLQO1zE-5DvFoRCtcnS77S5OvoZlMW7LoyFJwhJoLp8JgxZpaqU6fmIqm" alt="Spare Parts" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" />
          </div>
          <div class="p-10">
            <h3 class="text-2xl font-bold mb-4">Original Spare Parts</h3>
            <p class="text-on-surface-variant mb-8 leading-relaxed">
              Kami hanya menggunakan suku cadang original Fujitsu untuk memastikan kompatibilitas dan durabilitas maksimal bagi perangkat Anda.
            </p>
            <ul class="space-y-3 mb-10">
              <li class="flex items-center gap-2 text-sm text-on-surface-variant">
                <Icon name="material-symbols:check-circle" class="text-primary text-lg" />
                Pick Roller & Pad Assembly
              </li>
              <li class="flex items-center gap-2 text-sm text-on-surface-variant">
                <Icon name="material-symbols:check-circle" class="text-primary text-lg" />
                Genuine ADF Assemblies
              </li>
            </ul>
            <NuxtLink to="/spare-parts" class="text-primary font-bold inline-flex items-center gap-2 group-hover:gap-4 transition-all">
              Cek Stok Spare Part
              <Icon name="material-symbols:arrow-right-alt" class="text-xl" />
            </NuxtLink>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
