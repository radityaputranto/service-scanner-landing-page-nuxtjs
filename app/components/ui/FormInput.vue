<script setup>
defineProps({
  label: { type: String, required: true },
  id: { type: String, required: true },
  type: { type: String, default: 'text' },
  modelValue: { type: [String, Number], default: '' },
  error: { type: String, default: '' },
  placeholder: { type: String, default: '' },
  isTextarea: { type: Boolean, default: false }
})

defineEmits(['update:modelValue', 'blur'])
</script>

<template>
  <div class="flex flex-col gap-1.5">
    <label :for="id" class="text-sm font-semibold text-on-surface-variant">{{ label }}</label>
    
    <textarea v-if="isTextarea" 
              :id="id" 
              :value="modelValue" 
              @input="$emit('update:modelValue', $event.target.value)"
              @blur="$emit('blur')"
              :placeholder="placeholder"
              class="px-4 py-3 rounded-lg border bg-surface-container-lowest focus:ring-2 focus:ring-primary focus:outline-none transition-colors"
              :class="[error ? 'border-red-500' : 'border-outline-variant hover:border-secondary']"
              rows="4"></textarea>
    
    <input v-else 
           :id="id" 
           :type="type" 
           :value="modelValue" 
           @input="$emit('update:modelValue', $event.target.value)"
           @blur="$emit('blur')"
           :placeholder="placeholder"
           class="px-4 py-3 rounded-lg border bg-surface-container-lowest focus:ring-2 focus:ring-primary focus:outline-none transition-colors"
           :class="[error ? 'border-red-500' : 'border-outline-variant hover:border-secondary']" />
           
    <span v-if="error" class="text-xs text-red-500 mt-1 flex items-center gap-1">
      <Icon name="material-symbols:error" class="text-sm" />
      {{ error }}
    </span>
  </div>
</template>
