// $(document).ready(function() {
//     var cartChangeUrl = $('#cart-change-url').val();
  
//     $('.increment, .decrement').click(function() {
//       var cartId = $(this).data('cart-id');
//       var action = $(this).hasClass('increment') ? 'increment' : 'decrement';
  
//       $.ajax({
//         url: cartChangeUrl,
//         method: 'POST',
//         data: {
//           'cart_id': cartId,
//           'action': action,
//           'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
//         },
//         success: function(response) {
//           // Оновити значення на сторінці
//           $('input[data-cart-id="' + cartId + '"]').val(response.quantity);
//           $('.product-price[data-cart-id="' + cartId + '"]').text(response.products_price + ' $');
//           $('.total-quantity').text(response.total_quantity);
//           $('.total-price').text(response.total_price + ' ₴');
//         },
//         error: function(response) {
//           console.log('Error:', response);
//         }
//       });
//     });
//   });
  