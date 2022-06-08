<template>
  <aside class="cart-container">
    <div class="cart">
      <h1 class="cart-title spread">
        <span>
          Minicart
          <i class="icofont-cart-alt icofont-1x"></i>
        </span>
        <button @click="toggle" class="cart-close">&times;</button>
      </h1>

      <div class="cart-body">
        <table class="cart-table">
          <thead>
            <tr>
              <th><span class="sr-only">Imágen del producto</span></th>
              <th>Producto</th>
              <th>Precio</th>
              <th>Cant</th>
              <th>Subt</th>
              <th><span class="sr-only">Acciones</span></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(quantity, key, i) in cart" :key="i">
              <td><i class="icofont-carrot icofont-3x"></i></td>
              <td>{{ key }}</td>
              <td>$ {{ getPrice(key) }}</td>
              <td class="center">{{ quantity }}</td>
              <td>${{ (quantity * getPrice(key)).toFixed(2) }}</td>
              <td class="center">
                <button class="btn btn-light cart-remove">&times;</button>
              </td>
            </tr>
          </tbody>
        </table>

        <p v-if="!Object.keys(cart).length" class="center">
          <em>Tu carrito está vacío</em>
        </p>
        <div class="spread">
          <span
            ><strong>Total:</strong> $ {{ calculateTotal() }}</span
          >
          <button class="btn btn-light">Confirmar Pedido</button>
        </div>
      </div>
    </div>
  </aside>
</template>

<script>
export default {
  props: ['toggle', 'cart', 'inventory'],
  computed: {
    cartTotal () {
      return (this.cart.carrot * 4.82).toFixed(2)
    }
  },
  methods: {
    getPrice (name) {
      const prod = this.inventory.find(p => p.name === name)
      return prod.price.USD
    },
    calculateTotal () {
      const cartEntries = Object.entries(this.cart)
      const total = cartEntries.reduce((tot, p) => {
        return tot + p[1] * this.getPrice(p[0])
      }, 0)

      return total.toFixed(2)
    }
  }
}
</script>
