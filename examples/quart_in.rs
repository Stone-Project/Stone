// stone:job stone:math.quart_in
// stone:function quart_in_rs

#[no_mangle]
pub extern "C" fn quart_in_rs(t: f64) -> f64 { t * t * t * t }
