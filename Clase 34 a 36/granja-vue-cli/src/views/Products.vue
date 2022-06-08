<template>
  <main class="wrapper">
    <h1 class="title">Productos</h1>
    <div class="products">
        <Card
          v-for="(prod, index) in inventory"
          :key="prod.id"
          :prod="prod"
          :inventory="inventory"
          :addToCart="addToCart"
          :index="index"
        />
    </div>
  </main>
</template>

<script>
import Card from '../components/Card'

export default {
  props: ['inventory', 'addToCart'],
  components: {
    Card
  }
}
</script>

<style>
  .title {
    color: red;
  }
</style>
