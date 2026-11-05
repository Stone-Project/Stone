// stone:job stone:math.quad_in
// stone:function quad_in_rs

#[no_mangle]
pub extern "C" fn quad_in_rs(t: f64) -> f64 { t * t }
