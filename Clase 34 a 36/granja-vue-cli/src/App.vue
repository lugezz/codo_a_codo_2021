<template>
  <header class="top-bar spread">
    <nav class="top-bar-nav">
      <router-link to="/" class="top-bar-link">
        <i class="icofont-spoon-and-fork"></i>
        <span>Home</span>
      </router-link>
      <router-link to="products" class="top-bar-link">
        <span>Productos</span>
      </router-link>
      <router-link to="past-orders" class="top-bar-link">
        <span>Historial de Pedidos</span>
      </router-link>
    </nav>
    <div @click="toggleSidebar" class="top-bar-cart-link">
      <i class="icofont-cart-alt icofont-1x"></i>
      <span>Minicart ({{ totalQuantity }})</span>
    </div>
  </header>
  <router-view v-if="dataReady" :inventory="inventory" :addToCart="addToCart" />
  <Sidebar
    v-if="showSidebar"
    :toggle="toggleSidebar"
    :cart="cart"
    :inventory="inventory"
  />
</template>

<script>
import Sidebar from './components/Sidebar'
export default {
  data () {
    return {
      showSidebar: false,
      dataReady: false,
      inventory: {},
      cart: {}
    }
  },
  async mounted () {
    const data = await (await fetch('http://localhost:5000/products')).json()
    this.inventory = data
    this.dataReady = true
  },
  computed: {
    totalQuantity () {
      return Object.values(this.cart).reduce((acc, curr) => {
        return acc + curr
      }, 0)
    }
  },
  methods: {
    addToCart (name, quantity) {
      this.cart[name] ??= 0
      this.cart[name] += quantity
    },
    toggleSidebar () {
      this.showSidebar = !this.showSidebar
    }
  },
  components: { Sidebar }
}
</script>
