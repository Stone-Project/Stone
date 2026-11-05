// stone:job stone:math.negate
// stone:function negate_rs

#[no_mangle]
pub extern "C" fn negate_rs(x: f64) -> f64 { -x }
