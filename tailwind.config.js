module.exports = {
  content: [
  './*.html',
  './node_modules/flowbite/**/*.js'
  ],
  darkMode: 'media',
  theme: {
    screens: {
      'sm': '440px',
      'md': '768px',
      'lg': '1024px',
      'xl': '1280px',
      '2xl': '1536px',
  },
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}
