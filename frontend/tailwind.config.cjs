/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html",'./src/**/*.{svelte,js,ts}'],
  theme: {
    fontFamily: {
      body: ['Comfortaa', 'Arial', 'cursive'],
      heading: ['Montserrat', 'Helvetica', 'Arial', 'sans-serif'],
      serif: ['Merriweather', 'Georgia', 'Cambria', "Times New Roman", 'Times', 'serif'],
      king: ['Kingthings','Merriweather', 'Georgia', 'Cambria', "Times New Roman", 'Times', 'serif']
    },
    extend: {
      colors:{
        paper: "#CB6"
      },
      boxShadow: {
        "booklet-r": '30px 0px 40px -40px rgba(0,0,0,0.75) inset',
        "booklet-l": '-30px 0px 40px -40px rgba(0,0,0,0.75) inset'
      },
      backgroundImage: {
        "paper-texture": 'url("https://www.transparenttextures.com/patterns/45-degree-fabric-light.png")'
      }
    },
  },
  corePlugins: {
    aspectRatio: false,
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/aspect-ratio'),
  ],
}
