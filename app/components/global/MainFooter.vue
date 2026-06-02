<template>
<footer class="bg-slate-100 dark:bg-slate-900 w-full py-12">
<div class="max-w-7xl mx-auto px-8 grid grid-cols-1 md:grid-cols-4 gap-12">
<div class="space-y-6">
<div class="text-lg font-bold text-slate-900 dark:white">Fujitsu Repair</div>
<p class="text-slate-500 dark:text-slate-400 font-inter text-xs tracking-wide leading-relaxed">
                    Pusat layanan perbaikan scanner spesialis Fujitsu dengan jangkauan layanan nasional dan standar kualitas terjamin.
                </p>
<div class="flex gap-4">
<a class="w-8 h-8 rounded-full bg-slate-200 flex items-center justify-center hover:text-red-700 transition-colors text-slate-600" href="#"><span class="material-symbols-outlined text-sm" data-icon="public">public</span></a>
<a class="w-8 h-8 rounded-full bg-slate-200 flex items-center justify-center hover:text-red-700 transition-colors text-slate-600" href="#"><span class="material-symbols-outlined text-sm" data-icon="share">share</span></a>
</div>
</div>
<div class="space-y-6">
<h4 class="text-sm font-bold text-slate-900">Layanan</h4>
<ul class="space-y-4">
<li><NuxtLink to="/services" class="text-slate-500 dark:text-slate-400 hover:text-red-600 transition-colors font-inter text-xs tracking-wide">Maintenance Rutin</NuxtLink></li>
<li><NuxtLink to="/services" class="text-slate-500 dark:text-slate-400 hover:text-red-600 transition-colors font-inter text-xs tracking-wide">On-site Repair</NuxtLink></li>
<li><NuxtLink to="/services" class="text-slate-500 dark:text-slate-400 hover:text-red-600 transition-colors font-inter text-xs tracking-wide">Pick-up Service</NuxtLink></li>
<li><NuxtLink to="/spare-parts" class="text-slate-500 dark:text-slate-400 hover:text-red-600 transition-colors font-inter text-xs tracking-wide">Spare Part Replacement</NuxtLink></li>
</ul>
</div>
<div class="space-y-6">
<h4 class="text-sm font-bold text-slate-900">Kontak Kami</h4>
<ul class="space-y-4">
<li class="flex items-start gap-3 text-slate-500 dark:text-slate-400 font-inter text-xs tracking-wide">
<span class="material-symbols-outlined text-red-700" data-icon="location_on">location_on</span>
                        Griyo mapan sentosa Waru, Sidoarjo
                    </li>
<li class="flex items-center gap-3 text-slate-500 dark:text-slate-400 font-inter text-xs tracking-wide">
<span class="material-symbols-outlined text-red-700" data-icon="call">call</span>
                        (+62) 811-334-285
                    </li>
<li class="flex items-center gap-3 text-slate-500 dark:text-slate-400 font-inter text-xs tracking-wide">
<span class="material-symbols-outlined text-red-700" data-icon="mail">mail</span>
                        support@fujitsurepair.id
                    </li>
</ul>
</div>
<div class="space-y-6">
<h4 class="text-sm font-bold text-slate-900">Tautan Cepat</h4>
<div class="flex flex-col gap-4">
<NuxtLink to="/about" class="text-slate-500 dark:text-slate-400 hover:text-red-600 transition-colors font-inter text-xs tracking-wide">Tentang Kami</NuxtLink>
<NuxtLink to="/portfolio" class="text-slate-500 dark:text-slate-400 hover:text-red-600 transition-colors font-inter text-xs tracking-wide">Portofolio</NuxtLink>
<NuxtLink to="/blog" class="text-slate-500 dark:text-slate-400 hover:text-red-600 transition-colors font-inter text-xs tracking-wide">Tips & Edukasi</NuxtLink>
<NuxtLink to="/contact" class="text-slate-500 dark:text-slate-400 hover:text-red-600 transition-colors font-inter text-xs tracking-wide">Global Support</NuxtLink>
</div>
</div>
</div>
<div class="max-w-7xl mx-auto px-8 mt-16 pt-8 border-t border-slate-200">
<p class="text-slate-500 dark:text-slate-400 font-inter text-xs tracking-wide">
                © 2024 Industrial Atelier. Authorized Fujitsu Service Solutions.
            </p>
</div>
</footer>
</template>