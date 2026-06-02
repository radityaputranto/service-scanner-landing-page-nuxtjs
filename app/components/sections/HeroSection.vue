<template>
  <section class="relative min-h-[870px] flex items-center overflow-hidden">
    <div class="absolute inset-0 z-0">
      <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuDdYZb8HzUPK6veUXIngdzbA1h3c0pbLC5n7p5H_p31-vIFRfF200mCpefbqb4sVDCVY0MCH3DaXOoQ7X1srpQquuorNTz3sfIRZpTlba11fly-QRhe0SS0YqWNS6d_1tCmGZ4zSiEs-FqVeaqi7fREdNIclKpw4L1giJawHFF4EbAa9ZT8WuYwpo8n-af5HQvrZnxde8Hqm2CRHgfKTCXGXgkxhuVSoyaZMVoVbjHsN9RLC7iE4wHG71k7J-1Ja5bFJ1W3FXj7P3Fu" alt="Scanner Sensor Background" class="w-full h-full object-cover opacity-10 grayscale" />
    </div>
    
    <div class="max-w-7xl mx-auto px-8 grid grid-cols-1 md:grid-cols-12 gap-12 items-center relative z-10 w-full pt-12 md:pt-0">
      <div class="md:col-span-7 reveal delay-100">
        <div class="inline-flex items-center gap-2 px-3 py-1 bg-primary-container/10 text-primary-container rounded-full mb-6">
          <Icon name="material-symbols:verified" class="text-lg text-primary" />
          <span class="text-xs font-bold uppercase tracking-wider">Expertise Terpercaya</span>
        </div>
        
        <h1 class="text-5xl md:text-7xl font-extrabold tracking-tighter text-on-surface mb-6 leading-[1.1]">
          15+ Tahun Menjaga <span class="text-primary">Presisi</span> Scanner Anda.
        </h1>
        
        <p class="text-lg text-on-surface-variant max-w-xl mb-10 leading-relaxed">
          Layanan reparasi scanner Fujitsu resmi dengan teknisi bersertifikat. Kami mengembalikan performa scanner industrial dan perkantoran Anda ke standar pabrikan dengan garansi penuh.
        </p>
        
        <div class="flex flex-wrap gap-4">
          <a href="https://wa.me/#" class="bg-[#25D366] text-white px-8 py-4 rounded-lg font-bold text-lg flex items-center gap-3 hover:shadow-2xl hover:scale-105 transition-all duration-300">
            <Icon name="material-symbols:chat" class="text-2xl" />
            Konsultasi Gratis
          </a>
          <NuxtLink to="/services" class="border border-outline-variant px-8 py-4 rounded-lg font-bold text-lg text-on-surface hover:bg-surface-container transition-colors">
            Lihat Layanan
          </NuxtLink>
        </div>
      </div>
      
      <div class="md:col-span-5 relative hidden md:block reveal delay-300">
        <div class="aspect-square bg-surface-container-high rounded-2xl overflow-hidden shadow-2xl relative rotate-3 hover:rotate-0 transition-transform duration-500">
          <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuBv8yydKysAPfZqUja6WlOjDwqEsJFXLGmwusk8YKIKyRdDtkpcSUkPq68m5STJxIAEwRKw-x8PGmTyfim9SRPT2TqDCSnmDuyRVZZkw35MHiU17kdo81q6Yti8xmvvNupOR7EPOV1P2rjubNpJ96CEK4jsGVWZUk_VwpSrV4FsskAvf83UxuI7IQrkJ4OelvFNzki0xNCqF-xxlYXMQMth3Kk8p1YV6ZmpmrEXC7rOgj4c8sgUXW7oy6oPjYEFIdt4y7INmbPXCp_z" alt="Technician working" class="w-full h-full object-cover" />
          <div class="absolute inset-0 bg-gradient-to-t from-primary/40 to-transparent"></div>
        </div>
        
        <!-- Floating Stat Card -->
        <div class="absolute -bottom-6 -left-12 bg-white p-6 shadow-xl rounded-lg border-l-4 border-primary hover:-translate-y-2 transition-transform duration-300">
          <div class="text-3xl font-extrabold text-primary mb-1">99.8%</div>
          <div class="text-sm font-medium text-secondary">Akurasi Perbaikan</div>
        </div>
      </div>
    </div>
  </section>
</template>
