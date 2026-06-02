<template>
<nav class="fixed top-0 w-full z-50 bg-white/60 dark:bg-slate-950/60 backdrop-blur-xl">
<div class="flex justify-between items-center max-w-7xl mx-auto px-8 h-20">
<NuxtLink to="/" class="text-xl font-bold tracking-tighter text-red-700 dark:text-red-500 uppercase">Fujitsu Repair</NuxtLink>
<div class="hidden md:flex items-center space-x-8">
<NuxtLink to="/" class="font-inter text-sm transition-colors" :class="$route.path === '/' ? 'text-red-700 dark:text-red-500 font-bold border-b-2 border-red-700' : 'text-slate-600 dark:text-slate-400 hover:text-red-700'">Home</NuxtLink>
<NuxtLink to="/services" class="font-inter text-sm transition-colors" :class="$route.path.startsWith('/services') ? 'text-red-700 dark:text-red-500 font-bold border-b-2 border-red-700' : 'text-slate-600 dark:text-slate-400 hover:text-red-700'">Layanan</NuxtLink>
<NuxtLink to="/spare-parts" class="font-inter text-sm transition-colors" :class="$route.path.startsWith('/spare-parts') ? 'text-red-700 dark:text-red-500 font-bold border-b-2 border-red-700' : 'text-slate-600 dark:text-slate-400 hover:text-red-700'">Spare Part</NuxtLink>
<NuxtLink to="/about" class="font-inter text-sm transition-colors" :class="$route.path.startsWith('/about') ? 'text-red-700 dark:text-red-500 font-bold border-b-2 border-red-700' : 'text-slate-600 dark:text-slate-400 hover:text-red-700'">Tentang Kami</NuxtLink>
<NuxtLink to="/portfolio" class="font-inter text-sm transition-colors" :class="$route.path.startsWith('/portfolio') ? 'text-red-700 dark:text-red-500 font-bold border-b-2 border-red-700' : 'text-slate-600 dark:text-slate-400 hover:text-red-700'">Portofolio</NuxtLink>
<NuxtLink to="/blog" class="font-inter text-sm transition-colors" :class="$route.path.startsWith('/blog') ? 'text-red-700 dark:text-red-500 font-bold border-b-2 border-red-700' : 'text-slate-600 dark:text-slate-400 hover:text-red-700'">Tips & Edukasi</NuxtLink>
</div>
<NuxtLink to="/contact" class="bg-primary-container text-on-primary px-6 py-2.5 rounded hover:bg-primary transition-all duration-200 font-inter text-sm font-semibold flex items-center gap-2">
                Kontak
                <span class="material-symbols-outlined text-sm" data-icon="arrow_forward">arrow_forward</span>
</NuxtLink>
</div>
</nav>
</template>