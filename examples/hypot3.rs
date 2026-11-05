// stone:job stone:math.hypot3
// stone:function hypot3_rs

#[no_mangle]
pub extern "C" fn hypot3_rs(a: f64, b: f64, c: f64) -> f64 { (a*a + b*b + c*c).sqrt() }
