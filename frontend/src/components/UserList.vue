<template>

  <div class='w-full flex flex-col gap-4 '>

    <div class='flex '>
      <UserForm @submit='refreshData'>
        <Button variant='default'>
          Add User
        </Button>
      </UserForm>
    </div>

    <!--  table for user info -->
    <template v-if='data.length === 0'>
      <div class='w-full h-32 flex items-center justify-center text-3xl font-bold'>
        <span class='i-fluent-border-none-24-regular text-3xl' />
        <span>暂无数据</span>
      </div>
    </template>
    <template v-else>
      <table>
        <thead>
        <tr>
          <th>Id</th>
          <th>Name</th>
          <th>Gender</th>
          <th>Action</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for='item in data' :key='item.uid'>
          <td>{{ item.uid }}</td>
          <td>{{ item.name }}</td>
          <td>{{ item.gender }}</td>
          <td>
            <UserForm @submit='refreshData' :user='item'>
              <Button variant='secondary'>
                Edit
              </Button>
            </UserForm>
          </td>
        </tr>
        </tbody>
      </table>

      <div class='flex flex-row gap-4 justify-end'>
        <div class='flex flex-row items-center justify-center gap-2'>
          <Input type='number' v-model='limit' class='w-16' @change='refreshData' /> 项 / 页
        </div>
        <div class='flex gap-2'>
          <Pagination v-slot='{ page }'
                      show-edges
                      :total='total'
                      :itemsPerPage='limit'
                      :page='page'
                      @update:page='(newPage) => {
                          page = newPage
                          refreshData()
                        }'
          >
            <PaginationList v-slot='{ items }' class='flex items-center gap-1'>
              <PaginationFirst />
              <PaginationPrev />

              <template v-for='(item, index) in items'>
                <PaginationListItem v-if="item.type === 'page'" :key='index' :value='item.value' as-child>
                  <Button class='w-10 h-10 p-0' :variant="item.value === page ? 'default' : 'outline'">
                    {{ item.value }}
                  </Button>
                </PaginationListItem>
                <PaginationEllipsis v-else :key='item.type' :index='index' />
              </template>

              <PaginationNext />
              <PaginationLast />
            </PaginationList>
          </Pagination>
        </div>
      </div>
    </template>

  </div>

</template>

<script setup lang='ts'>

import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import {
  Pagination,
  PaginationEllipsis,
  PaginationFirst,
  PaginationLast,
  PaginationList,
  PaginationListItem,
  PaginationNext,
  PaginationPrev
} from '@/components/ui/pagination'

import UserForm from '@/components/UserForm.vue'
import { getUserList, type User } from '@/lib/user'
import { computed, ref } from 'vue'

const data = ref<User[]>([])
const loading = ref(false)

const total = ref(0)
const page = ref(1)
const limit = ref(3)

const havePrev = computed(() => page.value > 1)

const haveNext = computed(() => {
  return page.value * limit.value < total.value
})

const refreshData = async () => {
  loading.value = true
  const paginationData = await getUserList(page.value, limit.value)
  loading.value = false

  data.value = paginationData.data
  total.value = paginationData.total
  page.value = paginationData.current_page
}

const afterAddUser = () => {
  refreshData()
}

const clickPrev = () => {
  if (havePrev.value) {
    page.value -= 1
    refreshData()
  }
}

const clickNext = () => {
  if (haveNext.value) {
    page.value += 1
    refreshData()
  }
}

refreshData()
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;

  th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: center;
    vertical-align: middle;
  }

  th {
    background-color: #f2f2f2;
  }
}

</style>
