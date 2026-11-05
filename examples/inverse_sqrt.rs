// stone:job stone:math.inverse_sqrt
// stone:function inverse_sqrt_rs

#[no_mangle]
pub extern "C" fn inverse_sqrt_rs(x: f64) -> f64 { 1.0 / x.sqrt() }
