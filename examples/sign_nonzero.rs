// stone:job stone:math.sign_nonzero
// stone:function sign_nonzero_rs

#[no_mangle]
pub extern "C" fn sign_nonzero_rs(x: f64) -> f64 {
    let a = if x > 0.0 { 1.0 } else { 0.0 };
    let b = if x < 0.0 { 1.0 } else { 0.0 };
    a - b
}
