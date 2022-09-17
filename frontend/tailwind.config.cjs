/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html",'./src/**/*.{svelte,js,ts}'],
  theme: {
    fontFamily: {
      body: ['Comfortaa', 'Arial', 'cursive'],
      heading: ['Montserrat', 'Helvetica', 'Arial', 'sans-serif']
    },
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}
