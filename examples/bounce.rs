// stone:job stone:math.bounce
// stone:function bounce_rs

#[no_mangle]
pub extern "C" fn bounce_rs(x: f64) -> f64 {
    1.0 - (x.rem_euclid(2.0) - 1.0).abs()
}
