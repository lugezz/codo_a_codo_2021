<template>
  <div class="home">
    <div class="splash-container">
      <div class="splash">
        <h1>Granjita VUE</h1>
      </div>
    </div>

    <main class="wrapper">
      <h1 class="title">Recomendados</h1>

      <div class="recommended">
        <Card
          v-for="(prod, index) in inventory.slice(0, 3)"
          :key="prod.id"
          :prod="prod"
          :inventory="inventory"
          :addToCart="addToCart"
          :index="index"
        />
      </div>
    </main>
  </div>
</template>

<script>
// @ is an alias to /src
import Card from '../components/Card'

export default {
  name: 'Home',
  props: ['inventory', 'addToCart'],
  components: {
    Card
  }
}
</script>
