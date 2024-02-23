<script setup lang='ts'>

import { Button } from '@/components/ui/button'
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle
} from '@/components/ui/dialog'
import { FormControl, FormField, FormItem, FormLabel, FormMessage } from '@/components/ui/form'
import { Input } from '@/components/ui/input'
import { Select, SelectContent, SelectGroup, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select'

import { addUser, GenderArray, updateUser, type User } from '@/lib/user'

import { toTypedSchema } from '@vee-validate/zod'
import { useForm } from 'vee-validate'
import { type PropType, ref, watchEffect } from 'vue'
import * as z from 'zod'

const props = defineProps({
  user: {
    type: Object as PropType<User | undefined>,
    required: false
  }
})
const open = defineModel('open', {
  value: {
    type: Boolean,
    required: true
  }
})
const emit = defineEmits([ 'submit' ])

const loading = ref(false)

const formSchema = toTypedSchema(z.object({
  name: z.string().min(2).max(50),
  gender: z.enum(GenderArray)
}))

const form = useForm({
  validationSchema: formSchema,
  initialValues: {
    name: '',
    gender: undefined
  }
})

watchEffect(() => {
  console.log('heheh', props.user)
  form.setValues({
    name: props.user?.name || '',
    gender: props.user?.gender
  })
  form.set
})

const onSubmit = form.handleSubmit(async (values) => {
  loading.value = true
  if (props.user) {
    await updateUser(props.user.uid, values.name, values.gender)
  } else {
    await addUser(values.name, values.gender)
  }
  loading.value = false

  form.resetForm({
    values: {
      name: '',
      gender: undefined
    }
  });
  open.value = false
  emit('submit')
})

</script>

<template>
  <Dialog v-model:open='open'>
    <DialogContent>
      <DialogHeader>
        <DialogTitle>
          {{ props.user ? 'Edit User' : 'Add User' }}
        </DialogTitle>
        <DialogDescription></DialogDescription>
      </DialogHeader>
      <form class='w-full space-y-6'>
        <FormField v-slot='{ componentField }' name='name'>
          <FormItem>
            <FormLabel>Name</FormLabel>
            <FormControl>
              <Input type='text' v-bind='componentField' />
            </FormControl>
            <FormMessage />
          </FormItem>
        </FormField>
        <FormField v-slot='{ componentField }' name='gender'>
          <FormItem>
            <FormLabel>Gender</FormLabel>
            <Select v-bind='componentField'>
              <FormControl>
                <SelectTrigger>
                  <SelectValue />
                </SelectTrigger>
              </FormControl>
              <SelectContent>
                <SelectGroup>
                  <SelectItem v-for='(item, index) in GenderArray' :key='index' :value='item'>
                    {{ item }}
                  </SelectItem>
                </SelectGroup>
              </SelectContent>
            </Select>
            <FormMessage />
          </FormItem>
        </FormField>
      </form>

      <DialogFooter>
        <DialogClose as-child>
          <Button type='button' variant='secondary'>
            Cancel
          </Button>
        </DialogClose>

        <Button type='submit' variant='default' :disabled='loading' @click='onSubmit'>
            <span v-if='loading'>
              <span class='i-fluent-sync-24-regular animate-spin' />
              Loading...
            </span>
          <span v-else>
              Submit
            </span>
        </Button>
      </DialogFooter>
    </DialogContent>
  </Dialog>
</template>

<style scoped>
</style>
