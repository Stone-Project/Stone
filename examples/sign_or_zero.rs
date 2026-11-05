// stone:job stone:math.sign_or_zero
// stone:function sign_or_zero_rs

#[no_mangle]
pub extern "C" fn sign_or_zero_rs(x: f64) -> f64 {
    if x < 0.0 { -1.0 } else if x > 0.0 { 1.0 } else { 0.0 }
}
