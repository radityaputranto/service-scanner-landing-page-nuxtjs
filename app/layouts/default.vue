<script setup>
// Default layout
</script>

<template>
  <div class="min-h-screen flex flex-col bg-surface text-on-surface selection:bg-primary-container selection:text-white">
    <MainHeader />
    <slot />
    <MainFooter />
  </div>
</template>
